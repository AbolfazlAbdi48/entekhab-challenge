from django.contrib.auth.forms import UserCreationForm

from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='ایمیل')
    first_name = forms.CharField(label='نام')
    last_name = forms.CharField(label='نام خانوادگی')
