# Generated by Django 4.2.5 on 2023-09-27 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_studentquery_currunt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquery',
            name='currunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 22, 12, 22, 69345)),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='curuunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 22, 12, 22, 69345)),
        ),
    ]
