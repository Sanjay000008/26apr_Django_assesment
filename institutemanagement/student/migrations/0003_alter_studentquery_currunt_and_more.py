# Generated by Django 4.2.5 on 2023-09-27 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentquery_alter_studentsignup_curuunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquery',
            name='currunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 22, 11, 33, 599395)),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='curuunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 22, 11, 33, 599395)),
        ),
    ]
