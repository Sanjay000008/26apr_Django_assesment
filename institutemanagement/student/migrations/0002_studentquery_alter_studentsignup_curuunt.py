# Generated by Django 4.2.5 on 2023-09-27 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currunt', models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 21, 18, 21, 225623))),
                ('query', models.CharField(max_length=100)),
                ('opt', models.CharField(max_length=100)),
                ('myfiles', models.FileField(upload_to='Files')),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='curuunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 27, 21, 18, 21, 224629)),
        ),
    ]
