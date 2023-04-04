# Generated by Django 3.2.13 on 2022-06-23 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_company_staff_employer_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_staff',
            name='current_employee_lastname',
        ),
        migrations.RemoveField(
            model_name='company_staff',
            name='current_employee_name',
        ),
        migrations.RemoveField(
            model_name='company_staff',
            name='employer_phone_number',
        ),
        migrations.RemoveField(
            model_name='scheduler_db',
            name='doctor_lastname',
        ),
        migrations.RemoveField(
            model_name='scheduler_db',
            name='doctor_name',
        ),
        migrations.AddField(
            model_name='company_staff',
            name='staff_lastname',
            field=models.CharField(default='default title', max_length=100, verbose_name='staff_lastname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_staff',
            name='staff_name',
            field=models.CharField(default='default title', max_length=100, verbose_name='staff_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_staff',
            name='staff_phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='staff_phone_number'),
        ),
        migrations.AddField(
            model_name='scheduler_db',
            name='staff_lastname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scheduler.company_staff'),
        ),
        migrations.AddField(
            model_name='scheduler_db',
            name='staff_name',
            field=models.CharField(default='default title', max_length=100, verbose_name='staff_name'),
            preserve_default=False,
        ),
    ]
