from django.contrib.auth import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_manager_main, name='task_manager'),
    path('make_work_schedule', views.make_work_schedule, name='make_work_schedule'),
    path('test', views.test, name='test'),
    ]