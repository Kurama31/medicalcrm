# -*- config: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf

# Сделать правильный редирект
# https://pythonpip.ru/django/django-perenapravlyaet-polnoe-rukovodstvo-po-redirektam

def login(request):
    args = {}
    args.update(csrf(request)) # Засовываем в словарь уникальный код csrf
    #print("args.update(csrf(request)): ", args.update(csrf(request)))
    if request.POST:
        # Получить из POST запроса username. Если ничего не то присвоится ''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) # -> если пользователь есть возврат моджели пользователя
        if user is not None:
            auth.login(request, user) # Создаёться сессия для этого пользователя
            #print("request.META.get('HTTP_REFERER') ", request.META.get('HTTP_REFERER'))
            #return redirect('/')
            # После аутентификации возвращает на страницу "ссылателя")))
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            args = {
                'login_error': "Пiльзователь нi найден"
            }
            #return render(request, 'loginsys/login.html', args)
            return render(request, 'main/Layout.html', args)
    # Default HttpResponse on `GET` requests
    return render(request, 'loginsys/login.html', args)

def logout(request):
    auth.logout(request)
    #return redirect("/")
    return redirect(request.META.get('HTTP_REFERER'))

def test(request):

    return redirect("https://vk.com/id5139576")
