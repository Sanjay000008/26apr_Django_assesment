from django.db import models
from datetime import datetime

# Create your models here.
class studentSignup(models.Model):
    curuunt=models.DateTimeField(default=datetime.now(),blank=True)
    fullname=models.CharField(max_length=50)
    dob=models.DateField()
    doj=models.DateField()
    username=models.EmailField()
    password=models.CharField(max_length=12)
    mobile=models.BigIntegerField()

    
    
class studentquery(models.Model):
    #created=models.DateTimeField(auto_now_add=True)
    currunt=models.DateTimeField(default=datetime.now(),blank=True)
    query=models.CharField(max_length=100)
    opt=models.CharField(max_length=100)
    myfiles=models.FileField(upload_to='Files')
    comments=models.TextField()
