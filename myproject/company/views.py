from django.shortcuts import render
from random import random, randrange
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.views import LoginView
from .forms import AdminLoginForm, CreateFoodForm, CreateFoodCategoryForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shoping.models import Purchase, UNIT_CHOICES
from django.http import JsonResponse

import time

# Create your views here.


class CompanyView(View):
    def get(self, request):
        #todo снизу стрка чтобы считать айдишник зарегавшего пользвователя
        user_id = request.user.id
        if request.user.is_authenticated and request.user.is_staff:
            context = {
                "message": "Админ панель",
            }
            return render(request, 'company/company.html', context=context)
        else:
            return HttpResponse("<h4>Ошибка, войдите за админа</h4>"
                                "<a href='/company/admin_login'>Войти</a>")


class AdminDjangoLogin(LoginView):
    form_class = AdminLoginForm
    template_name = 'company/admin_login.html'

    def get_success_url(self):
        return reverse_lazy('company_admin')


class CreateDjangoCategory(View):
    def get(self, request):
        form = CreateFoodCategoryForm(request.POST, request.FILES)
        context = {
            'form': form,
        }
        return render(request, 'company/create_category_food.html', context=context)

    def post(self, request):
        form = CreateFoodCategoryForm(request.POST)
        if form.is_valid():
                category_data = form.save(commit=False)
                category_data.save()
                return HttpResponseRedirect('/company/list_category/')
                #return HttpResponse(f"<h4>Была создана категория</h4>")
        else:
            return HttpResponse("<h4>Ошибка, форма недействительна</h4>")


class CreateDjangoFood(View):
    def get(self, request):
        form = CreateFoodForm(request.POST, request.FILES)

        context = {
            'form_food': form,
        }
        return render(request, 'company/create_food.html', context=context)

    def post(self, request):
        form = CreateFoodForm(request.POST, request.FILES)
        if form.is_valid():
            food_data = form.save(commit=False)
            food_data.save()
            return HttpResponseRedirect('/company/list_food/')
        else:
            return HttpResponse("<h4>Ошибка</h4>")



class CategoryListView(View):
    def get(self, request):
        categorys = FoodCategory.objects.all()

        """Пагинация по всем категориям"""
        page = request.GET.get('page', 1)
        paginator = Paginator(categorys, 5)
        categorys = paginator.get_page(page)
        try:
            categorys = paginator.page(page)
        except PageNotAnInteger:
            categorys = paginator.page(1)
        except EmptyPage:
            categorys = paginator.page(paginator.num_pages)



        context = {
            "message":"Список категорий",
            "categorys":categorys
        }
        return  render(request, 'company/list_categorys.html', context=context)

class FoodListView(View):
    def get(self, request):
        foods = Food.objects.all()

        """Пагинация по всем категориям"""
        page = request.GET.get('page', 1)
        paginator = Paginator(foods, 5)
        foods = paginator.get_page(page)
        try:
            foods = paginator.page(page)
        except PageNotAnInteger:
            foods = paginator.page(1)
        except EmptyPage:
            foods = paginator.page(paginator.num_pages)



        context = {
            "message":"Список продуктов",
            "foods":foods
        }
        return  render(request, 'company/list_foods.html', context=context)

class FoodDetailView(View):
    def get(self, request, **kwargs):
        food = Food.objects.get(pk=kwargs['pk'])
        context = {
            "message": "Карточка еды",
            "food":food,
        }
        return render(request, 'company/food_detail.html', context=context)

class FoodEditView(View):
    def get(self, request, **kwargs):
        food = Food.objects.get(pk=kwargs['pk'])
        form = CreateFoodForm(request.POST or None, instance=food)
        form.id = food.id
        context = {
        "message": "Редактирование еды",
        "form": form,
        }
        return render(request, 'company/food_edit.html', context=context)

class FoodSaveView(View):
     def post(self, request):
         food = Food.objects.get(pk=request.POST.get('id'))
         form = CreateFoodForm(request.POST or None, request.FILES or None, instance=food)
         if form.is_valid():
            form.save(commit=True)
         return redirect('list_food_admin')


class FoodRemoveView(View):
    def get(self, request, **kwargs):
        Food.objects.filter(pk=kwargs['pk']).update(visibility=False)
        return redirect('list_food_admin')

class FoodUndoRemoveView(View):
    def get(self, request, **kwargs):
        Food.objects.filter(pk=kwargs['pk']).update(visibility=True)
        return redirect('list_food_admin')

#для категорий№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
class CategoryDetailView(View):
    def get(self, request, **kwargs):
        category = FoodCategory.objects.get(pk=kwargs['pk'])
        context = {
            "message": "Карточка категории",
            "category":category,
        }
        return render(request, 'company/category_detail.html', context=context)

class CategoryEditView(View):
    def get(self, request, **kwargs):
        category = FoodCategory.objects.get(pk=kwargs['pk'])
        form = CreateFoodCategoryForm(request.POST or None, instance=category)
        form.id = category.id
        context = {
        "message": "Редактирование категории",
        "form": form,
        }
        return render(request, 'company/category_edit.html', context=context)

class CategorySaveView(View):
     def post(self, request):
         category = FoodCategory.objects.get(pk=request.POST.get('id'))
         form = CreateFoodCategoryForm(request.POST or None, request.FILES or None, instance=category)
         if form.is_valid():
            form.save(commit=True)
         return redirect('list_category_admin')


#Для управления заказами
@login_required
def admin_panel(request):
    if not request.user.is_staff:
        return redirect('home')
    purchases = Purchase.objects.all()
    context = {
        'purchases': purchases,
        'unit_choices': UNIT_CHOICES
    }
    return render(request, 'company/edit_purchase.html', context)

# @login_required
# def update_purchase_status(request, purchase_id):
#     if not request.user.is_staff:
#         return redirect('home')
#     purchase = Purchase.objects.get(id=purchase_id)
#     if request.method == 'POST':
#         status = request.POST.get('status')
#         purchase.status = status
#         purchase.save()
#         messages.success(request, f'Статус заказа {purchase.id} изменен на {status}.')
#         return redirect('processing_admin')
#     context = {
#         'purchase': purchase,
#         'unit_choices': UNIT_CHOICES
#     }
#     return render(request, 'company/update_purchase_status.html', context)

def update_purchase_status(request):
    if request.method == 'POST':
        purchase_id = request.POST.get('purchase_id')
        status = request.POST.get('status')
        try:
            purchase = Purchase.objects.get(id=purchase_id)
            purchase.status = status
            purchase.save()
            time.sleep(2)
            return JsonResponse({'status': 'ok', 'new_status': purchase.get_status_display()})
        except Purchase.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Purchase not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


from django.core.files.storage import FileSystemStorage
# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         file = request.FILES['file']
#         fs = FileSystemStorage()
#         fs.save(file.name, file)
#         return render(request, 'company/upload_file.html')
#     return render(request, 'company/upload_file.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        employee_file = EmployeeFileModel(file=file)
        employee_file.save()
        messages.success(request, 'Файл успешно загружен.')
        return redirect('upload_file')
    return render(request, 'company/upload_file.html')