from django.urls import path
from apps.scheduler.models import Scheduler_DB, company_staff
from apps.scheduler.views import staff_selector_views
from apps.scheduler import views as create_event
from apps.scheduler import views as test


from . import views


urlpatterns = [
#    path('', scheduler_views.scheduler, name='scheduler_main'),
    #today/
    path('', views.staff_selector_views, name="scheduler_today"),
    path('test', views.test, name='test_views'),
    path('work_days', views.work_days,  name='work_days'),
    path('<str:productid>', views.create_new_event, name='create_new_event'),


]



# ---------------------------------------------------------------------------
#WORK 01
#urlpatterns = [
#    path('',
#         ArchiveIndexView.as_view(model=Scheduler_DB, date_field="date_begin"),
#         name="scheduler_main"),
#]

