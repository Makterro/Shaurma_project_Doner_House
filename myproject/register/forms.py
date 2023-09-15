from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=11,
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': "field"}))
    password = forms.CharField(
        max_length=30,
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': "field"}))

class RegisterUserForm(forms.ModelForm):
    field_order = ['login', 'password', 'password2']

    password = forms.CharField(
        max_length= 24,
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Введите пароль',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        max_length=24,
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Подтвердите пароль',
                'class': 'form-control'
            }
        ),
        help_text=("Введите тот же самый пароль для проверки")
    )

    class Meta:
        model = User

        fields = ['username', 'email']

        exclude = ["is_blocked"]

        labels = {
            'username': 'Логин',
            'email': 'E-mail',
        }


