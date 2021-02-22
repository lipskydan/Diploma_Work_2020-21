from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Ім’я', max_length=30, required=False, help_text='Необов’язково', localize=True)
    last_name = forms.CharField(label='Прізвище', max_length=30, required=False, help_text='Необов’язково', localize=True)
    email = forms.EmailField(label='Поштова адреса', max_length=254, help_text='Вимагається. Повідомте дійсну електронну адресу', localize=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(label='Ім’я')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
