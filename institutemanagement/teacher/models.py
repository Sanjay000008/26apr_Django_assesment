from django.db import models
from datetime import datetime

# Create your models here.
class teacherSignup(models.Model):
    curuunt=models.DateTimeField(default=datetime.now(),blank=True)
    fullname=models.CharField(max_length=50)
    dob=models.DateField()
    doj=models.DateField()
    username=models.EmailField()
    password=models.CharField(max_length=12)
    compensation=models.CharField(max_length=255)
    mobile=models.BigIntegerField()
