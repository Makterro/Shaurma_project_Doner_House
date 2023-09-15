from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CompanyView.as_view(), name='company_admin'),
    path('admin_login/', AdminDjangoLogin.as_view(), name='login_admin'),
    path('create_category/', CreateDjangoCategory.as_view(), name='create_product_category_admin'),
    path('create_food/', CreateDjangoFood.as_view(), name='create_product_admin'),
    path('list_category/', CategoryListView.as_view(), name='list_category_admin'),
    path('list_food/', FoodListView.as_view(), name='list_food_admin'),
    path('processing/', admin_panel, name='processing_admin'),
    # path('processing/update/<int:purchase_id>/', update_purchase_status, name='processing_update_admin'),
    path('processing/update/', update_purchase_status, name='processing_update_admin'),
    path('upload_employee/', upload_file, name='upload_file'),

    path('food/detail/<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('food/edit/<int:pk>/', FoodEditView.as_view(), name='food_edit'),
    path('food/save/', FoodSaveView.as_view(), name='food_save'),
    path('food/remove/<int:pk>/', FoodRemoveView.as_view(), name='food_remove'),
    path('food/undo_remove/<int:pk>/', FoodUndoRemoveView.as_view(), name='food_undoremove'),

    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/edit/<int:pk>/', CategoryEditView.as_view(), name='category_edit'),
    path('category/save/', CategorySaveView.as_view(), name='category_save'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
