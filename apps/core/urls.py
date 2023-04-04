from django.urls import path
from apps.core import views as core_views

urlpatterns = [
    path('', core_views.main, name='main-url')
]