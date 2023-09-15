from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Food, FoodCategory

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Введите логин"
            }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Введите пароль"
            }
        )
    )

class CreateFoodForm(forms.ModelForm):

    class Meta:
        model = Food

        fields = [ 'name', 'ingredients','photo', 'mini', 'mini_gram',
                   'medium','medium_gram', 'mega', 'mega_gram', 'value', 'category']
        exclude = ['visibility']
        labels = {
            'name': 'Название',
            'ingredients': 'Ингредиенты',
            'photo': 'Фотография',
            'mini': 'Мини',
            'mini_gram': 'Мини грамм',
            'medium':'Средняя',
            'medium_gram': 'Средняя грамм',
            'mega': 'Мега',
            'mega_gram': 'Мега грамм',
            'value': 'Значение',
            'category': 'Категория',
        }


class CreateFoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name', 'visibility']
        labels = {
            'name': 'Название категории',
            'visibility': 'Видимость',
        }
