from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from register.models import *
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart_items = Korzina.objects.filter(user=request.user.id)
        total_price = 0
        for item in cart_items:
            food = item.id_food
            if item.size == 'mini':
                item.total_price = item.quantity * food.mini
                item.price_per_item = food.mini
            elif item.size == 'medium':
                item.total_price = item.quantity * food.medium
                item.price_per_item = food.medium
            elif item.size == 'mega':
                item.total_price = item.quantity * food.mega
                item.price_per_item = food.mega
            total_price += item.total_price
        return render(request, 'shoping/cart.html', {'cart_items': cart_items, 'total_price': total_price})


class PurchaseView(View):
    def get(self, request, *args, **kwargs):
        cart_items = Korzina.objects.filter(user=request.user)
        total_price = 0
        for item in cart_items:
            food = item.id_food
            if item.size == 'mini':
                item.total_price = item.quantity * food.mini
                item.price_per_item = food.mini
            elif item.size == 'medium':
                item.total_price = item.quantity * food.medium
                item.price_per_item = food.medium
            elif item.size == 'mega':
                item.total_price = item.quantity * food.mega
                item.price_per_item = food.mega
            total_price += item.total_price
        return render(request, 'shoping/purchase.html', {'cart_items': cart_items, 'total_price': total_price})

    def post(self, request, *args, **kwargs):
        cart_items = Korzina.objects.filter(user=request.user)
        total_price = 0
        for item in cart_items:
            food = item.id_food
            if item.size == 'mini':
                item.total_price = item.quantity * food.mini
                item.price_per_item = food.mini
            elif item.size == 'medium':
                item.total_price = item.quantity * food.medium
                item.price_per_item = food.medium
            elif item.size == 'mega':
                item.total_price = item.quantity * food.mega
                item.price_per_item = food.mega
            total_price += item.total_price

        payment = request.POST.get('payment')

        try:
            payment = float(payment)
        except ValueError:
            messages.error(request, 'Введите корректную сумму оплаты')
            return redirect('purchase')

        if payment < total_price:
            messages.error(request, 'Сумма оплаты меньше стоимости заказа')
            return redirect('purchase')
        elif payment > total_price:
            messages.error(request, 'Сумма оплаты больше стоимости заказа')
            return redirect('purchase')
        else:
            purchase = Purchase.objects.create(user=request.user, payment_received=True, total_price=total_price)
            for item in cart_items:
                if item.size == 'mini':
                        purchase_item = PurchaseItem.objects.create(
                            purchase=purchase,
                            food=item.id_food,
                            quantity=item.quantity,
                            size=item.size,
                            price=item.id_food.mini,
                        )
                elif item.size == 'medium':
                        purchase_item = PurchaseItem.objects.create(
                            purchase=purchase,
                            food=item.id_food,
                            quantity=item.quantity,
                            size=item.size,
                            price=item.id_food.medium,
                        )
                elif item.size == 'mega':
                        purchase_item = PurchaseItem.objects.create(
                            purchase=purchase,
                            food=item.id_food,
                            quantity=item.quantity,
                            size=item.size,
                            price=item.id_food.mega,
                        )

            cart_items.delete()
            messages.success(request, 'Оплата прошла успешно')
            return HttpResponseRedirect("/", locals())


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'purchases'
    paginate_by = 10

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user).order_by('-date_created')

class PurchaseDetailView(LoginRequiredMixin, DetailView):
    model = Purchase
    template_name = 'shoping/purchase_detail.html'
    context_object_name = 'purchase'

    def get_object(self):
        purchase_id = self.kwargs.get('purchase_id')
        purchase = get_object_or_404(Purchase, id=purchase_id, user=self.request.user)
        return purchase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        purchase = self.get_object()
        purchase_items = PurchaseItem.objects.filter(purchase=purchase)
        context['purchase_items'] = purchase_items
        return context