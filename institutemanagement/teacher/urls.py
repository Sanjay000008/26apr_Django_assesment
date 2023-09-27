from django.contrib import admin
from django.urls import path,include
from teacher import views

urlpatterns = [
    path('',views.index),
    path('teacher/',views.teacher,name='teacher'),
    path('teachersprofile/',views.teachersprofile,name='teachersprofile'),
]