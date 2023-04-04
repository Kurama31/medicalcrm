from django.contrib import admin
from apps.task_manager.models import task_manager_work_days, task

admin.site.register(task_manager_work_days)
admin.site.register(task)
