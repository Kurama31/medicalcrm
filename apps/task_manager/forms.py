from .models import task_manager_work_days, task
from django.forms import ModelForm, TextInput, DateTimeInput


class task_manager_work_days_Form(ModelForm):
    class Meta:
        # с какой моделью работаем
        model = task_manager_work_days
        # поля, которые будут внутри формы ПОЛЬЗОВАТЕЛЮ
        fields = ['date_begin', 'date_end', 'user_id', 'status']  # 'date', 'profile_id', 'status'
        # default = False

        widgets = {
            "date_begin": DateTimeInput(attrs={
                # 'type': 'date'
            }),
            "date_end": DateTimeInput(attrs={
                'class': 'form-control',
                # 'placeholder': 'Название статьи'
            })
        }


# 'class': 'CheckboxInput'
class task_Form(ModelForm):
    class Meta:
        # с какой моделью работаем
        model = task
        # поля, которые будут внутри формы ПОЛЬЗОВАТЕЛЮ
        fields = ['title', 'description', 'task_making_date', 'task_begin_date',
                  'deadline', 'completed', 'task_author', 'task_executor', 'user_id']
