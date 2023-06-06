import calendar
import copy
import datetime

from pprint import pprint

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.main.my_classes import my_date
from apps.task_manager.models import task_manager_work_days, task
from .forms import task_manager_work_days_Form, task_Form

now = datetime.datetime.now()


def get_calendar(slected_period) -> str:
    # slected_period be like "2023-05"
    selected_year = int(slected_period[:4])
    selected_month = int(slected_period[5:])
    current_month = calendar.monthcalendar(selected_year, selected_month)
    month_data_begin = []
    test_data_end = []

    for index, item_data_begin in enumerate(current_month):
        for i, day in enumerate(item_data_begin):

            if day == 0 and day < 10:
                item_data_begin[i] = '0'
            # elif day != 0 and day < 10:
            #    item_data_begin[i] = str(today.year) + '-' + str(today.month) + '-0' + str(day) + 'T' + '09:00'
            else:
                # item_data_begin[i] = str(today.year) + '-' + str(f'{today.month:02}') + '-' + str(f'{day:02}') + 'T' + '09:00'
                item_data_begin[i] = str(selected_year) + '-' + str(f'{selected_month:02}') + '-' + str(
                    f'{day:02}') + 'T' + '09:00'

        month_data_begin.append(item_data_begin)
    data_begin_calendar = copy.deepcopy(month_data_begin)

    for index, item in enumerate(month_data_begin):
        for i, day in enumerate(item):
            if day != '0':
                item[i] = item[i][:10] + 'T00:00'
        test_data_end.append(item)
    data_min_lim = copy.deepcopy(test_data_end)

    for index, item in enumerate(month_data_begin):
        for i, day in enumerate(item):
            if day != '0':
                item[i] = item[i][:10] + 'T23:59'
        test_data_end.append(item)

    data_max_lim = copy.deepcopy(test_data_end)

    return data_begin_calendar, data_min_lim, data_max_lim


# def select_interval_of_days():


def select_color(current_month_list, user_id):
    select_color_by_status_list = copy.deepcopy(current_month_list)

    for index, single_week_list in enumerate(select_color_by_status_list):
        for index_2, single_day_dict in enumerate(single_week_list):
            if single_day_dict['date_begin'] == '0' and single_day_dict['user_id'] == user_id:
                # Нет дня недели в месяце (дата = 0)
                if single_day_dict['status'] == '0':
                    color_of_the_day = 'red'
                single_week_list[index_2] = single_day_dict
            elif single_day_dict['date_begin'] != '0' and single_day_dict['user_id'] == user_id:
                # Рабочий (отмеченный) день в месяце (дата != 0)
                if single_day_dict['status'] == '1':
                    color_of_the_day = 'green'
                # НЕ Рабочий (не отмеченный) день в месяце (дата != 0)
                elif single_day_dict['status'] == '0':
                    color_of_the_day = 'blue'

            select_color_by_status_list[index][index_2] = color_of_the_day

    return select_color_by_status_list


def make_work_schedule(request):
    # now = datetime.datetime.now()
    get_auth = auth.get_user(request).username  # получить пользователя из реквеста
    get_user_id = auth.get_user(request).id

    # ============== Select month ==============

    user_selected_month = dict(request.GET)
    if user_selected_month:
        selected_year = user_selected_month['selected_month'][0][:4]
        selected_month = user_selected_month['selected_month'][0][5:]
        slected_period = user_selected_month['selected_month'][0]
    else:
        selected_year = now.year
        selected_month = now.month
        slected_period = str(selected_year) + '-' + str(f'{selected_month:02}')

    # /============== END Select month ==============

    form = task_manager_work_days.objects.all().filter(user_id=get_user_id,
                                                       date_begin__year=selected_year,
                                                       date_begin__month=selected_month).order_by('date_begin')

    # ============== CREATE default items (NEW month) ==============

    select_default_calendar_all = get_calendar(slected_period)
    select_default_calendar = select_default_calendar_all[0]
    # new_month_list = []
    # print("====================================== form", form)
    # print("-------------------------------------- time 1", get_user_id, selected_year, selected_month)
    for single_week in select_default_calendar:
        for i, single_day in enumerate(single_week):
            if single_day == '0':
                single_day_dict = {
                    "date_begin": '0',
                    "date_end": '0',
                    "user_id": get_user_id,
                    "status": "0"
                }
                single_week[i] = single_day_dict
            elif single_day != '0':
                single_day_dict = {
                    "date_begin": str(single_day),
                    "date_end": str(single_day[:10]) + 'T18:00',
                    "user_id": get_user_id,
                    "status": "0"
                }
                single_week[i] = single_day_dict
    new_month_list = copy.deepcopy(select_default_calendar)

    # ============== select_default_items (NEW month) ==============

    # =============== Повторная запись в БД или АПДЛЕЙТ =======================
    if form.exists():
        # print("There is at least one object in form")
        request_status = "Запись у этого юзера за этот месяц уже есть"
        submit_button = "KURWA еж!"
        # Форматирование данных из формы для отправки в шаблон ===============================================================

        for index, single_week_list in enumerate(new_month_list):
            for index_2, single_day_dict in enumerate(single_week_list):
                if single_day_dict['date_begin'] == '0' and single_day_dict['user_id'] == get_user_id:
                    single_week_list[index_2] = single_day_dict
                elif single_day_dict['date_begin'] != '0' and single_day_dict['user_id'] == get_user_id:
                    for data_in_form in form:
                        if single_day_dict['date_begin'][:10] == str(data_in_form.date_begin.date()):
                            single_day_dict = {
                                "date_begin": str(data_in_form.date_begin.date()) + 'T' + str(
                                    data_in_form.date_begin.time())[:5],
                                "date_end": str(data_in_form.date_end.date()) + 'T' + str(data_in_form.date_end.time())[
                                                                                      :5],
                                "user_id": data_in_form.user_id,
                                "status": data_in_form.status
                            }

                    single_week_list[index_2] = single_day_dict

        # current_month_list Для отображения данных из БД если они есть
        current_month_list = new_month_list
        # print("we take this current_month_list (from DB )")

        # ============== Для записи в БД =====================================

        if request.method == 'POST':
            form_recording = task_manager_work_days_Form(request.POST)

            # Проверить и может быть убрать is_valid()
            if form_recording.is_valid():

                QueryDict = request.POST
                myDict = dict(QueryDict)
                Query_list = []

                for key, value in myDict.items():
                    Query_list.append({key: value})
                objects_list = []

                for index, data_list in enumerate(Query_list[1]['date_begin']):
                    get_date_begin = Query_list[1]['date_begin'][index]

                    if get_date_begin != '':
                        d = datetime.datetime.strptime(get_date_begin, "%Y-%m-%dT%H:%M")
                        date_begin_parsed = d.strftime("%Y-%m-%d %H:%M:%S")
                        # Парсим date_end в нужную базе форму
                        get_date_end = Query_list[2]['date_end'][index]
                        d = datetime.datetime.strptime(get_date_end, "%Y-%m-%dT%H:%M")
                        date_end_parsed = d.strftime("%Y-%m-%d %H:%M:%S")

                        objects_list.append({
                            'date_begin': date_begin_parsed,
                            'date_end': date_end_parsed,
                            'status': Query_list[3]['status'][index],
                            'user_id': Query_list[4]['user_id'][index]
                        })

        # ============== UPDATE записей В БД ==============
        user_bulk_update_list = []
        if request.method == 'POST':

            batch = [task_manager_work_days(
                date_begin=row['date_begin'],
                date_end=row['date_end'],
                user_id=row['user_id'],
                status=row['status']
            ) for row in objects_list]

            # user_id = user_id в исходниках для начальный данных
            for updated_data in form:
                # 15.05.2023 issues: WHAT is that:?
                updated_data.status = updated_data.status

                for batch_data in batch:
                    if str(batch_data.date_begin)[:10] == str(updated_data.date_begin.date()):

                        if str(batch_data.date_begin) != str(updated_data.date_begin.date()) + ' ' + str(
                                updated_data.date_begin.time()) or str(batch_data.date_end) != str(
                            updated_data.date_end.date()) + ' ' + str(updated_data.date_end.time()) \
                                or batch_data.status != updated_data.status:
                            updated_data.date_begin = datetime.datetime.strptime(batch_data.date_begin,
                                                                                 "%Y-%m-%d %H:%M:%S")
                            updated_data.date_end = datetime.datetime.strptime(batch_data.date_end, "%Y-%m-%d %H:%M:%S")
                            updated_data.status = batch_data.status

                            user_bulk_update_list.append(updated_data)

            task_manager_work_days.objects.bulk_update(user_bulk_update_list,
                                                       ['date_begin', 'date_end', 'user_id', 'status'])
            print("========updated_data===========", updated_data)
            # ============== END UPDATE записей В БД ==============
            return redirect(request.build_absolute_uri())

    else:
        # print("There is no one object in form, so we START: ")
        request_status = "У этого юзера за этот месяц НЕТ записей. вообще!"
        submit_button = "Отправить "  # Я пердолил!!

        # ============== Первая ЗАПИСЬ В БД ==============
        print("========UPLOAD data 01.05. issues 00===========")
        print("request.method: ", request.method)
        if request.method == 'POST':
            form_recording = task_manager_work_days_Form(request.POST)

            if form_recording.is_valid():
                print("========UPLOAD data 01.05. issues 01===========")
                QueryDict = request.POST
                myDict = dict(QueryDict)
                Query_list = []

                for key, value in myDict.items():
                    Query_list.append({key: value})
                objects_list = []

                for index, data_list in enumerate(Query_list[1]['date_begin']):
                    get_date_begin = Query_list[1]['date_begin'][index]

                    if get_date_begin != '':
                        d = datetime.datetime.strptime(get_date_begin, "%Y-%m-%dT%H:%M")
                        date_begin_parsed = d.strftime("%Y-%m-%d %H:%M:%S")
                        # Парсим date_end в нужную базе форму
                        get_date_end = Query_list[2]['date_end'][index]
                        d = datetime.datetime.strptime(get_date_end, "%Y-%m-%dT%H:%M")
                        date_end_parsed = d.strftime("%Y-%m-%d %H:%M:%S")

                        objects_list.append({
                            'date_begin': date_begin_parsed,
                            'date_end': date_end_parsed,
                            'status': Query_list[3]['status'][index],
                            'user_id': Query_list[4]['user_id'][index]
                        })

                batch = [task_manager_work_days(
                    date_begin=row['date_begin'],
                    date_end=row['date_end'],
                    user_id=row['user_id'],
                    status=row['status']
                ) for row in objects_list]
                task_manager_work_days.objects.bulk_create(batch)

                request_status = "Запись добавлена "
                return redirect(request.build_absolute_uri())
            else:
                request_status = "Запить в БД с успехом провалена : "
                return redirect(request.build_absolute_uri())

        current_month_list = copy.deepcopy(new_month_list)

    # /============== END ЗАПИСЬ В БД ==============
    select_color_by_status_list = select_color(current_month_list, get_user_id)
    data = {
        'username': get_auth,
        'error': 'Request failed successfully',
        'slected_period': slected_period,
        'get_user_id': get_user_id,
        'request_status': request_status,
        'calendar': get_calendar(slected_period),
        'current_month_list': current_month_list,
        'submit_button': submit_button,
        'select_color': select_color_by_status_list
    }

    return render(request, 'task_manager/make_work_schedule.html', data)


def time_select_list():
    minutes_list = []
    hours_list = []
    time_picker_list = []

    minutes = -15
    while minutes != 45:
        minutes += 15
        minutes_list.append(f'{minutes:02}')

    hours = -1
    while hours != 23:
        hours += 1
        hours_list.append(f'{hours:02}')

    for hours_and_minuts in hours_list:
        for minuts_swap in minutes_list:
            time_picker_list.append(hours_and_minuts + ':' + minuts_swap)
    return time_picker_list


def iteration_hours():
    hours_list = []
    # hours = -1
    hours_begin = 8
    hours_end = 20
    while hours_begin != hours_end:
        hours_begin += 1
        hours_list.append(f'{hours_begin:02}')

    return hours_list


def make_data_from_2_str(input_list):
    single_date_str = input_list[0]['tmd_DATE'][0]
    single_time_str = input_list[1]['tmd_TIME'][0]
    # print(single_date_str)
    # print(single_time_str)
    lock_up_date = str(single_date_str + ' ' + single_time_str)
    # print(lock_up_date)
    return lock_up_date


def days_shift(selector_of_days_interval):
    # Только ФИКСИРОВАННЕ периоды может будет лучше?
    # list_of_days = []
    if selector_of_days_interval == 5:
        two_days = datetime.timedelta(2)
        date_begin = now - two_days
        days_end = now + two_days
        warp = 1
    elif selector_of_days_interval == 10:
        days = datetime.timedelta(5)
        date_begin = now - days
        days_end = now + days
        warp = 0
    else:
        two_days = datetime.timedelta(2)
        date_begin = now - two_days
        days_end = now + two_days
        warp = 1



    delta = days_end - date_begin

    #list_of_days = [(date_begin + datetime.timedelta(i)).strftime("%d") for i in range(delta.days + warp)]
    list_of_dates = [(date_begin + datetime.timedelta(i)).strftime("%Y-%m-%d") for i in range(delta.days + warp)]
    list_of_days = [x[8:] for x in list_of_dates]

    return date_begin, days_end, list_of_days, list_of_dates


# print("----------------------------------------",days_shift()[3])

# The real task manager
# Отобразить все задачи пользователя
def task_manager_main(request):
    get_auth = auth.get_user(request).username
    # user_last_name = auth.get_user(request).username
    get_user_id = auth.get_user(request).id
    # value="2018-06-12T19:30" для HTML

    # ============== Select month ==============

    user_selected_month = dict(request.GET)
    print("user_selected_month: ", user_selected_month)

    #print("user_selected_month: ", type(int(user_selected_month['amount_of_days'][0])), user_selected_month['amount_of_days'][0])
    if user_selected_month:
        selected_year = user_selected_month['selected_month'][0][:4]
        selected_month = user_selected_month['selected_month'][0][5:]
        slected_period = user_selected_month['selected_month'][0]

        number_of_days = int(user_selected_month['amount_of_days'][0])
    else:
        selected_year = now.year
        selected_month = now.month
        slected_period = str(selected_year) + '-' + str(f'{selected_month:02}')

        number_of_days = 5
    # Переписать на ДЕКОРАТОР!
    # /============== END Select month ==============

    form = task.objects.all().filter(user_id=get_user_id,
                                     task_begin_date__year=selected_year,
                                     task_begin_date__month=selected_month).order_by('deadline')
    pprint(form)
    # print("data from form: ", form[0])
    """
    for x in form:
        print("queryset_data: ", x.task_begin_date.day)

    list_of_days = [x.task_begin_date.day for x in form]
    print("list_of_days ", list_of_days)
    """
    # tasks = task.objects.filter(user_id=get_user_id).order_by('deadline')
    # .all().filter(user_id=get_user_id, task_begin_date=days_shift()[0] )

    # Определяем дату создания задания
    now_raw = datetime.datetime.now()
    # now = str(now_raw.date()) + 'T' + str(now_raw.time())[:5]
    # datetime.datetime.strptime(myDict['tmd_DATE'][0] + ' ' + myDict['tmd_TIME'][0],"%Y-%m-%d %H:%M")
    if request.method == 'POST':
        QueryDict = request.POST
        myDict = dict(QueryDict)
        print("myDict: ", myDict)
        print("deadline ", my_date.date_to_db(myDict['deadline'][0]))
        batch1 = task(
            title=myDict['title'][0],
            description=myDict['description'][0],
            task_making_date=str(now_raw.date()) + 'T' + str(now_raw.time())[:5],
            task_begin_date=my_date.composite_date(myDict['tmd_DATE'][0], myDict['tmd_TIME'][0]),
            deadline=my_date.date_to_db(myDict['deadline'][0]),
            completed=myDict['completed'][0],
            task_author=get_auth,
            task_executor=myDict['task_executor'][0],
            user_id=get_user_id
        )

        task.save(batch1)
        return redirect('task_manager')

    error = "Вы совершили недопустимое действие. Ваш компьютер будет взорван, а вы расстреляны!"
    # print("DATE BEGIN!!!!", days_shift()[0])

    users = User.objects.all().values()

    users_list = [str(user['id']) + ' ' + user['username'] + ' ' + user['first_name'] + ' ' + user['last_name'] for user
                  in users]

    # ======= select interval of days ======
    # composite_date = my_date.composite_date

    #
    print("select_interval_of_days: ", now.strftime("%Y-%m-%d"))  # T%H:%M

    data = {
        'form': form,
        'tasks': form,  # FOR TEST
        'username': get_auth,
        'slected_period': slected_period,
        'time_picker_list': time_select_list(),
        'users_list': users_list,
        'hours_list': iteration_hours(),
        'list_of_days': days_shift(number_of_days)[2],
        'list_of_dates': days_shift(number_of_days)[3],
        'list_of_data': get_calendar(slected_period)
    }
    # pprint(data)
    # pprint(form)
    return render(request, 'task_manager/task_manager_main.html', data)


# Personal task manager
"""
def task_manager_main(request):
    error = 'task_manager_main'
    # Авторизация пользователя тут! (логика в loginsys)
    get_auth = auth.get_user(request).username  # получить пользователя из реквеста
    data = {
        'form': 'form',
        'username': get_auth,
        'error': error
    }

    return render(request, 'task_manager/task_manager_main.html', data)
"""


# Manager's task manager
def test(request):
    return render(request, 'task_manager/test.html')
