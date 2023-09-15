from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    #Вывод в читаемом виде
    list_display = [field.name for field in Food._meta.fields]
    #Редактируемые поля
    list_editable = ("name","ingredients", "visibility",
                     "mini", "mini_gram", "medium", "medium_gram",
                     "mega", "mega_gram", "value")
    # Список полей, по которым будет поиск в таблице
    search_fields = ['name']
    # Список полей, по которым будут фильтроваться записи в админке (панель)
    list_filter = ['name']

    class Meta:
        model = Food

class CategoryAdmin(admin.ModelAdmin):
    #Вывод в читаемом виде
    list_display = [field.name for field in FoodCategory._meta.fields]
    #Редактируемые поля
    list_editable = ['name']
    # Список полей, по которым будет поиск в таблице
    search_fields = ['name']
    # Список полей, по которым будут фильтроваться записи в админке (панель)
    list_filter = ['name']

    class Meta:
        model = FoodCategory


# Register your models here.
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, CategoryAdmin)