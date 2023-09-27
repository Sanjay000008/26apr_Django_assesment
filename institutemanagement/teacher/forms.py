from django import forms
from teacher.models import teacherSignup


class TeacherSignupForm(forms.ModelForm):
    class Meta:
        model=teacherSignup
        fields='__all__'


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model=teacherSignup
        fields=['fullname','dob','doj','username','password','compensation','mobile']