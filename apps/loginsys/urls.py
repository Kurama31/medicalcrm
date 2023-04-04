from django.contrib.auth import views
from django.urls import path
from . import views


# r'^' - значит что этот адрес подойдёт к любому юрл
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test, name='test'),
    ]