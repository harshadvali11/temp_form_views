from django import forms

from app.models import *

class Student(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(max_value=28)


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'