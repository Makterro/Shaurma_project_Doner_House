from django.urls import path, re_path
from .views import *
from  django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RegisterViev.as_view(), name='register_user'),
    path('login/', LoginViev.as_view(), name='login_user'),
    path('logout/', user_logout, name='logout_user'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)