from django.db import models


# Create your models here.
class task_manager_work_days(models.Model):
    date_begin = models.DateTimeField('date_begin', null=True, blank=True)
    date_end = models.DateTimeField('date_end', null=True, blank=True)
    status = models.CharField('is_working_day', null=True, blank=True, max_length=1)
    user_id = models.IntegerField('user_id', unique_for_date="date_begin")

#unique_for_date="date_begin"
    # Для того что б выводить список одним из вариантов
    def __str__(self):
        return self.status

    # указывает имя таблице в панели администратора
    class Meta:
        verbose_name = 'Рабочее расписание'

# due_date срок выполнения
class task(models.Model):
    title = models.CharField('title', max_length=200, null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)
    task_making_date = models.DateTimeField('task_making_date', null=True, blank=True)
    task_begin_date = models.DateTimeField('task_begin_date', null=True, blank=True)

    deadline = models.DateTimeField('deadline', null=True, blank=True)
    completed = models.CharField('completed', null=True, blank=True, max_length=1)
    task_author = models.CharField('task_author', null=True, blank=True, max_length=200)
    task_executor = models.CharField('task_executor', null=True, blank=True, max_length=200)
    user_id = models.IntegerField('user_id')



    def __str__(self):
        return self.title

    # указывает имя таблице в панели администратора
    class Meta:
        verbose_name = 'Таблица задач'