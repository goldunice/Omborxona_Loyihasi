from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarView.as_view()),
    path('mahsulotlar/', MahsulotlarView.as_view()),
    path('mijozlar/', MijozlarView.as_view()),
]
