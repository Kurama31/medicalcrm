# Generated by Django 3.2.10 on 2022-04-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_alter_scheduler_db_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheduler_db',
            options={'verbose_name': 'Расписание 0', 'verbose_name_plural': 'Расписание'},
        ),
        migrations.AlterField(
            model_name='scheduler_db',
            name='Doctor_lastname',
            field=models.CharField(max_length=100, verbose_name='Doctor_lastname'),
        ),
        migrations.AlterField(
            model_name='scheduler_db',
            name='cabinet_number',
            field=models.CharField(max_length=3, verbose_name='cabinet_number'),
        ),
        migrations.AlterField(
            model_name='scheduler_db',
            name='client_lastname',
            field=models.CharField(max_length=100, verbose_name='client_lastname'),
        ),
        migrations.AlterField(
            model_name='scheduler_db',
            name='client_name',
            field=models.CharField(max_length=100, verbose_name='client_name'),
        ),
        migrations.AlterField(
            model_name='scheduler_db',
            name='doctor_name',
            field=models.CharField(max_length=100, verbose_name='doctor_name'),
        ),
    ]
