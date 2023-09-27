from django.contrib import admin
from .models import *
# Register your models here.

class studentSignupClass(admin.ModelAdmin):
    list_display=['id','fullname','dob','doj','mobile']

class studentqueryClass(admin.ModelAdmin):
    list_display=['id','query','opt','myfiles','comments']

admin.site.register(studentSignup,studentSignupClass)
admin.site.register(studentquery,studentqueryClass)