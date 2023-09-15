from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, default='Не назначено')
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.name


GRAMS = 'GL'
MILLILITERS = 'ML'
Item = 'It'
Litr = 'Lt'
UNIT_CHOICES = [
    (GRAMS, 'Г'),
    (MILLILITERS, 'Мл'),
    (Item, 'Шт'),
    (Litr, 'Литр')
]

class Food(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    ingredients = models.CharField(max_length=128, blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    visibility = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='food_photos/')
    category = models.ForeignKey(FoodCategory, blank=False, null=False, on_delete=models.CASCADE)

    mini = models.IntegerField(blank=True, null=True, default=0)
    mini_gram = models.IntegerField(blank=True, null=True, default=0)

    medium = models.IntegerField(blank=False, null=False, default=0)
    medium_gram = models.IntegerField(blank=True, null=True, default=0)

    mega = models.IntegerField(blank=True, null=True, default=0)
    mega_gram = models.IntegerField(blank=True, null=True, default=0)
    value = models.CharField(max_length=128, choices=UNIT_CHOICES, blank=False, null=False,
                             default=GRAMS)  # грамм литр, миллитров




class EmployeeFileModel(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name

