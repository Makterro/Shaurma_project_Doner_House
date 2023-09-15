from random import random, randrange
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.

class RegisterViev(View):
    def get(self, request):
        #Для каптчи
        code = randrange(1121, 9899)
        global str_code
        str_code = str(code)

        form = RegisterUserForm(request.POST, request.FILES)

        context = {
            'form': form,
            'captcha': str_code
        }

        return render(request, 'register/register.html', context=context)

    def post(self, request):
        # todo Нужно сделать так, чтобы не регистрировать пользователя если его логин уже есть
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            captcha = request.POST.get('captcha')
            if str_code == str(captcha):
                if form.cleaned_data['password'] == form.cleaned_data['password2']:
                    log = form.cleaned_data.get('username')
                    passw = form.cleaned_data.get('password')
                    email = form.cleaned_data.get('email')

                    new_user = User.objects.create_user(username=log, password=passw, email=email)
                    login(request, new_user)
                    return HttpResponse(f"<h4>Вы создали аккаунт и уже вошли в него</h4>"
                                        f"<a href='/'>Перейти на главную страницу</a> </")
                else:
                    error = "Пароли не совпадают"
                    return render(request, 'register/register.html', context={'form': form, 'error': error})
            else:
                error = "Капча не совпадает"
                return render(request, 'register/register.html', context={'form': form, 'error': error})


class LoginViev(View):
    def get(self, request):
        form = LoginForm

        context = {
            'form': form,
            'message': 'Войдите в систему'
        }
        return render(request, 'register/login.html', context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            log = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=log, password=password)

            # print(login, password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect("/", locals())
            else:
                error = "Пользователь не активен"
                return render(request,'register/login.html', context={'form': form, 'error': error})
        else:
            return HttpResponseRedirect("register/login", locals())

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/", locals())