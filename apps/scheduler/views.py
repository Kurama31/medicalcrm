# scheduler

from apps.scheduler.models import Scheduler_DB, company_staff, Origin
from .forms import SchedulerForm
from django.shortcuts import render, redirect
from datetime import datetime, date


def staff_selector_views(request):
    staff_selector = company_staff.objects.all()
    staff_list = []
    for s_list in staff_selector:
        obj_to_str = str(s_list)
        staff_list.append(obj_to_str)
    print(staff_list)
    # =======================================================================
    select_1_row = Scheduler_DB.objects.all().filter(date_begin__gte=date.today())
    for select_event in select_1_row:
        # select_event - str
        print(select_event)
        # Одна запись потому что на "сегодня" и staff_list[0] = романов
        if select_event.staff_lastname == staff_list[0] and select_event.date_begin.hour == "9":
            print('======== ', str(select_event.date_begin.hour))
            print('======== ', type(str(select_event.date_begin.hour)))
        else:
            print('======== ', str(select_event.date_begin.hour))
            print("does not work")
    form = ''
    # =======================================================================

    error = 'staff_selector_views'
    data = {
        'form': form,
        'staff_list': staff_list,
        'error': error,
        'values': ['some', '123']
    }
    #print('form: ', form.values())
    return render(request, 'scheduler/scheduler_today.html', data)


def test(request):
    #today_raw = str(date.today())
    #today = int(today_raw[-2:])
    #print('today: ', today)
    #print("_________________________________")
    #form = Scheduler_DB.objects.all().filter(date_begin__day=today)   #.order_by('-date_begin')   #.filter(date_begin=datetime.today().date())
    form = Scheduler_DB.objects.all().filter(date_begin__gte=date.today())

    form_1 = company_staff.objects.all()

    form_2 = Origin.objects.all()
    error = 'staff_selector_views'
    data = {
        'form': form,
        'form_1': form_1,
        'form_2': form_2,
        'error': error,
        'values': ['some', '123']
    }
    #print('form: ', form.values())
    return render(request, 'scheduler/test.html', data)

"""
# РАБОЧИЙ вариант, но не понятно как с ним работать кроме повседневного представления
class ArticleTodayArchiveView(TodayArchiveView):
    queryset = Scheduler_DB.objects.all().order_by('-date_begin')
    date_field = "date_begin"
    allow_future = True
    allow_empty = True
    # scheduler_db + суфикс _archive_day.html = адрес искомой старницы
    # session
    #print(queryset)
    class PersonDetail(DetailView):
        model = Scheduler_DB

        def get_context_data(self, **kwargs):
            phones = Scheduler_DB.objects.all()
            context = super().get_context_data(**kwargs)
            context["phones"] = phones
            return context
"""


def create_new_event(request, productid):
    print("_________________________________11", productid)

    params = productid.split(sep=',')

    start_time_from_html = params[0]
    end_time_from_html = params[1]
    today = str(date.today())
    sep_data = today.split(sep='-')
    date_time_begin = sep_data[2] + '.' + sep_data[1] + '.' + sep_data[0] + ' ' + start_time_from_html
    date_time_end = sep_data[2] + '.' + sep_data[1] + '.' + sep_data[0] + ' ' + end_time_from_html
    #print(date_time_begin)

    #print(params[0])
    initial_dict = {
        "date_begin": date_time_begin,
        "date_end": date_time_end,
        "comment": "Запись на приём",
        "staff_name": str(params[2]),
        "staff_lastname": str(params[3])
    }
    # Для отображения и автоматического заполнения бланка формы
    error = 'Отображание формы create_new_event'
    # initial = initial_dict - запись в полях формы по умолчанию
    form = SchedulerForm(initial=initial_dict)

    # Отправляем из формы с указанием  <form  method="post". иф для того что б точно получать только отправку данных, а не что то ещё
    # Запускаеться только после нажатии кнопки сохранения!!!!
    if request.method == 'POST':
        # request.POST - ту находяться все данные получаемые с формы
        form = SchedulerForm(request.POST) # request.POST or None


        if form.is_valid(): # Обязательная проверка на заполнение!!!
            # сохраняет данные в табличке которую используем в методе
            form.save()
            return redirect('scheduler_today')
        else:
            error = 'ЗРАДА! (create_new_event > if request.method == )'
        # data - Словарь для передачи данных в .html РЫЗНЫХ ДАННЫХ!!!
    data = {
        'form': form,
        'error': error
    }
    print("_______________________here")
    return render(request, 'scheduler/create_new_event.html', data)


def work_days(request):
    return render(request, 'scheduler/test.html')

#today_raw = str(date.today())
#today = int(today_raw[-2:])
#form = Scheduler_DB.objects.all().filter(date_begin__day=today)   #.order_by('-date_begin')   #.filter(date_begin=datetime.today().date())
# =======================================================================