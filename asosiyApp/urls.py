from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarView.as_view(), name='sections'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='products'),
    path('mijozlar/', MijozlarView.as_view(), name='clients'),
    path('update_mahsulot/<int:num>/', UpdateMahsulot.as_view(), name='update'),
    path('delete_mahsulot/<int:num>/', DeleteMahsulot.as_view(), name='delete'),
    path('update_mijoz/<int:num>/', UpdateMijoz.as_view(), name='update_mijoz'),
    path('delete_mijoz/<int:num>/', DeleteMijoz.as_view(), name='delete_mijoz'),
]
