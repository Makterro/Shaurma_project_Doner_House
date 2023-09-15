from django import forms
from django.shortcuts import render


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', initial=1, min_value=1)
    # size = forms.ChoiceField(choices=[('mini', 'Мини'), ('medium', 'Средняя'), ('mega', 'Мега')], label='Размер')

