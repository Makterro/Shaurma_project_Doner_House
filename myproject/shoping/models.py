from django.db import models
from django.contrib.auth.models import User
from register.models import Food

# Create your models here.
NEW = 'new'
CANCEL = 'cancel'
START = 'start'
COOKING = 'cooking'
READY = 'ready'
SUCCESS = 'success'
UNIT_CHOICES = [
    (NEW, 'Не принят в обработку'),
    (CANCEL, 'Отменен'),
    (START, 'Принят в обработку'),
    (COOKING, 'Готовят'),
    (READY, 'Заказ готов'),
    (SUCCESS, 'Заказ завершен'),
]
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_received = models.BooleanField(default=False)
    status = models.CharField(max_length=128, choices=UNIT_CHOICES, blank=False, null=False, default=NEW)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=128, default='medium')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)