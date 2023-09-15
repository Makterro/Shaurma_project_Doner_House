from email.policy import default

from django.db import models
from django.contrib.auth.models import User
from company.models import Food

# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=128, blank=True, null=True, default=None)

class Korzina(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, default=None, on_delete=models.CASCADE)
    id_food = models.ForeignKey(Food, blank=False, null=False, default=None, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False, default=None)
    size = models.CharField(max_length=128, blank=False, null=False, default='medium')




