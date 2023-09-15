from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('add_food/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('food/detail/<int:pk>/', FoodDetailView.as_view(), name='landing_food_detail'),
    path('contacts/', ContactsView.as_view(), name='contact'),
    path('employment/', employment, name='employment'),
    path('check_file_status/', check_file_status, name='check_file_status'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
