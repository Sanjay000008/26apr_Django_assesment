# Generated by Django 4.2.5 on 2023-09-27 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curuunt', models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 22, 11, 33, 607350))),
                ('fullname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('doj', models.DateField()),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('compensation', models.CharField(max_length=255)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
