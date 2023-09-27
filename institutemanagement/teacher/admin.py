from django.contrib import admin
from .models import *
# Register your models here.

class teacherSignupClass(admin.ModelAdmin):
    list_display=['id','fullname','dob','doj','mobile','compensation']


admin.site.register(teacherSignup,teacherSignupClass)

# Register your models here.
