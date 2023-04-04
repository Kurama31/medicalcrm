

from apps.scheduler.models import Scheduler_DB
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, CheckboxInput


# ModelForm - класс, от которого всё наследуем
class SchedulerForm(ModelForm):
    # Meta - указываются характеристики для нашего класса
    #prepopulated_fields = {'client_name': ('client_lastname'),}
    class Meta:
        # с какой моделью работаем
        model = Scheduler_DB
        # поля, которые будут внутри формы
        fields = ['status', 'date_begin', 'date_end', 'comment', 'client_name',
                  'client_lastname', 'staff_name', 'staff_lastname', 'cabinet_number']

        widgets = {
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'is active'
            }),
            "date_begin": DateTimeInput(attrs={
                'class': 'DateTimeInput',
                'placeholder': 'Дата и время начала приёма',
                #'type': 'datetime-local'
            }),
            "date_end": DateTimeInput(attrs={
                'class': 'DateTimeInput',
                'placeholder': 'Дата и время окончания приёма',
                #'type': 'datetime-local'
            }),
            "comment": Textarea(attrs={
                #'class': 'CheckboxInput',
                'placeholder': 'Комментарий'
                #'format_value': 'test value'
            }),
            "client_name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Имя клиента'
            }),
            "client_lastname": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия клиента'
            }),
            "staff_name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Врача'
            }),
            "staff_lastname": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия врача'

            }),
            "cabinet_number": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Номер кабинета, где будет приём'
            })
        }

# doctor_lastname

"""
Рабочий выпадающий список 
"staff_lastname": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия врача',
                'type': 'Select'

"""

"""

from django import forms
# Работает ХРЕНОВИНА!
class SchedulerForm(forms.Form):
    date_begin = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
"""
