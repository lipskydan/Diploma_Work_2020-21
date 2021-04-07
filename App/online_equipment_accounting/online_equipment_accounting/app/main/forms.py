from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import widgets


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логін', required=True, help_text='Обов’язково', localize=True,
                               widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль', required=True, help_text='Обов’язково', localize=True,
                                widget=widgets.PasswordInput(attrs={'size': 1, 'class': 'form-control'}))
    password2 = forms.CharField(label='Підтвердження пароля', required=True, help_text='Обов’язково', localize=True,
                                widget=widgets.PasswordInput(attrs={'size': 1, 'class': 'form-control'}))

    first_name = forms.CharField(label='Ім’я', max_length=30, required=False, help_text='Необов’язково', localize=True,
                                 widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
    last_name = forms.CharField(label='Прізвище', max_length=30, required=False, help_text='Необов’язково',
                                localize=True,
                                widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))

    email = forms.EmailField(label='Поштова адреса', max_length=254, localize=True,
                             help_text='Обов’язково. Повідомте дійсну електронну адресу',
                             widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
    image = forms.ImageField(required=False, label='Фото користувача', max_length=254, localize=True,
                             help_text='Необов’язково',
                             widget=widgets.FileInput(attrs={'size': 1, 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image')


class LoginForm(forms.Form):
    username = forms.CharField(label='Ім’я', widget=widgets.TextInput(attrs={'size': 1, 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'size': 1, 'class': 'form-control'}))
