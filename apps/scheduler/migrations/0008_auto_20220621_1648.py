# Generated by Django 3.2.13 on 2022-06-21 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20220531_1805'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promise',
        ),
        migrations.AlterModelOptions(
            name='company_staff',
            options={'verbose_name': 'Персонал компании', 'verbose_name_plural': 'Персонал компании'},
        ),
    ]
