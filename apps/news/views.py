from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'

def news_home(request: render):
    # создаём класс news, objects - указвает что мы получаем все обьекты
    # можно получать из колонки. .all() указывает что все записи
    # [:2] кол-во записей, order_by сортировка
    # {'news': news} - то что выводит записи
    # Articles Таблица в БД,
    news = Articles.objects.order_by('-date')[:2]
    return render(request, 'news/news.html', {'news': news})

# Во вьюхе обрабатываеться маетод
def create(request):
    error = ''
    if request.method == 'POST':
        print("request: ", request.POST)
        # request.POST - все данные которые мы получили со страницы ввода (Для передачи в БД)
        form = ArticlesForm(request.POST)
        print("request.form: ", form)
        # is_valid - позволяет прояерить являються ли данные корректно заполненны
        if form.is_valid():
            # сохраняет данные в табличке которую используем в методе
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной. Смерть неверным!'

    form = ArticlesForm()
    # Объект form для передачи в html файл create.html
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)