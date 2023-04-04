import category as category
import objects
from django.db import models
from django.urls import reverse


# Create your models here.
class company_staff(models.Model):
    status = models.CharField('is active', max_length=1, default="1")
    date_begin = models.DateTimeField('date_begin')
    date_end = models.DateTimeField('date_end', null=True, blank=True)
    comment = models.CharField('comment', max_length=300, null=True, blank=True)
    staff_name = models.CharField('staff_name', max_length=100)
    staff_lastname = models.CharField('staff_lastname', max_length=100)
    staff_phone_number = models.CharField('staff_phone_number', max_length=11, null=True, blank=True)

    # Для того что б выводить список одним из вариантов
    def __str__(self):
        return self.staff_lastname

    # указывает имя таблице в панели администратора
    class Meta:
        verbose_name = 'Персонал компании'
        # тут в множественном числе
        verbose_name_plural = 'Персонал компании'


class Scheduler_DB(models.Model):
    status = models.CharField('is active', max_length=1, default="1")
    date_begin = models.DateTimeField('date_begin')
    date_end = models.DateTimeField('date_end')
    comment = models.CharField('comment', max_length=300, null=True, blank=True)
    client_name = models.CharField('client_name', max_length=100)
    client_lastname = models.CharField('client_lastname', max_length=100)
    staff_name = models.CharField('staff_name', max_length=100)
    staff_lastname = models.CharField('staff_lastname', max_length=100, unique_for_date='date_begin')
    cabinet_number = models.CharField('cabinet_number', max_length=3)

    # Для того что б выводить список одним из вариантов
    def get_absolute_url(self):
        return reverse('Scheduler-detail', kwargs={'pk': self.pk})

    # указывает имя таблице в панели администратора
    class Meta:
        verbose_name = 'Расписание 0'
        # тут в множественном числе
        verbose_name_plural = 'Расписание'

# (blank=True)

#print("return of Scheduler_DB is: ", Scheduler_DB.objects.all().values())
#print("return of Scheduler_DB 2 is: ", list(Scheduler_DB.objects.all().values()) )

#TEST 2


#--- TEST

class Origin(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
