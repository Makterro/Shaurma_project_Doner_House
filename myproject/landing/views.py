from random import random, randrange
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from company.models import Food, FoodCategory, EmployeeFileModel
from .forms import *
from itertools import groupby
from operator import attrgetter
from django.shortcuts import get_object_or_404
from register.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse

# Create your views here.
class MainView(View):
    def get(self, request):
        categories = FoodCategory.objects.filter(visibility=True)  # получаем все категории где видимость true
        category_list = []
        for category in categories:
            food = Food.objects.filter(category=category, visibility=True)  # получаем все товары
            category_dict = {'category': category, 'food': food}
            category_list.append(category_dict)

        #чтобы посчитать кол во товаров в корзине пользователя
        if request.user.is_authenticated:
            cart_items_count = Korzina.objects.filter(user=request.user).count()
        else: cart_items_count = None
        context = {
            'category_list': category_list,
            'cart_items_count': cart_items_count,
        }

        return render(request, 'landing/main.html', context=context)

    def post(self, request):
        pass



@login_required
def add_to_cart(request, **kwargs):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            size = request.POST.get('portion', None)
            #todo мне нужно считать значение с portion
            print(size)

            if not size:
                food_id = kwargs['pk']
                error_message = 'Выберите размер порции'
                return HttpResponseRedirect(
                    reverse('landing_food_detail', args=[food_id]) + f"?error_message={error_message}")

            food = get_object_or_404(Food, id=kwargs['pk'])

            Korzina.objects.create(
                user=request.user,
                id_food=food,
                quantity=quantity,
                size=size,
            )

            return HttpResponseRedirect(reverse_lazy('main'))
    else:
        form = AddToCartForm()
        return render(request, 'landing/detail.html', {'form': form})


class FoodDetailView(View):
    def get(self, request, **kwargs):
        form = AddToCartForm(request.POST)
        food = Food.objects.get(pk=kwargs['pk'])
        context = {
            "message": "Добавление еды в корзину",
            "food": food,
            "form": form
        }
        return render(request,'landing/detail.html', context=context)

    def post(self, request, **kwargs):
        #todo не понятно, почему не рабоатет с этим пост, пришлось сверху еще один создать
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            size = form.cleaned_data['size']

            food = get_object_or_404(Food, id=kwargs['pk'])

            if size == 'mini':
                price = food.mini
            elif size == 'medium':
                price = food.medium
            else:
                price = food.mega

            Korzina.objects.create(
                id_userdata=request.user,
                id_food=food,
                quantity=quantity,
                price=price
            )

            return reverse_lazy('main')

#Для контактов
class ContactsView(View):
    @method_decorator(cache_page(5))  # Кэширование на 5 секунд
    def get(self, request):
        return render(request, 'landing/contacts.html')



#Для трудоустройства
def check_file_status(request):
    try:
        file = EmployeeFileModel.objects.latest('id').file
        if file:
            status = 'ready'  # Готов к скачиванию
        else:
            status = 'not_ready'  # Файл не загружен
    except EmployeeFileModel.DoesNotExist:
        status = 'not_ready'  # Файл не загружен

    return JsonResponse({'status': status})

def employment(request):
    try:
        file_url = EmployeeFileModel.objects.latest('id').file.url
    except EmployeeFileModel.DoesNotExist:
        file_url = None

    return render(request, 'landing/employment.html', {'file_url': file_url})
