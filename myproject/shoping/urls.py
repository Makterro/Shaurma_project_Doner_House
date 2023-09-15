from django.urls import path, re_path
from .views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('purchase/', PurchaseView.as_view(), name='purchase'),

    path('list/', PurchaseListView.as_view(), name='purchase_list'),
    path('list/detail/<int:purchase_id>/', PurchaseDetailView.as_view(), name='purchase_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)