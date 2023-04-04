from django.urls import path
from apps.news import views as news_views


urlpatterns = [
    path('', news_views.news_home, name='news_home'),
    # news/create
    path('create', news_views.create, name='create')
]
# + static(myproject.STATIC_URL, document_root=myproject.STATIC_ROOT)