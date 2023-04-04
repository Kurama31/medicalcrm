from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.main import views as core_views

urlpatterns = [
    path('', core_views.main, name='main-url'),
    path('about_us/', core_views.about, name='about_us'),
    #path('news/', core_views.schedule)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)