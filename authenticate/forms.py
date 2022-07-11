from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from. models import Customuser


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]


class UserregisterForm(forms.ModelForm):
    class Meta:
        model=Customuser
        fields=['usertype']

