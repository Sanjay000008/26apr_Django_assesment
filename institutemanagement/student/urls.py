from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.index),
    path('studentQuery',views.studentQuery,name='studentQuery'),
    path('student/',views.student,name='student'),
    path('studentprofile/',views.studentprofile),
    path('userlogout/',views.userlogout),
]