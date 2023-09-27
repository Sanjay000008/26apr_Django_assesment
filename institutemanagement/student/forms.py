from django import forms
from student.models import studentSignup,studentquery


class StudentSignupForm(forms.ModelForm):
    class Meta:
        model=studentSignup
        fields='__all__'


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model=studentSignup
        fields=['fullname','dob','doj','username','password','mobile']

class StudentQueryform(forms.ModelForm):
    class Meta:
        model=studentquery
        fields='__all__'

