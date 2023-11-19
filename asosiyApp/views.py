from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bolimlar.html')
        else:
            return redirect('/')


class MahsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
                "user": request.user.username.capitalize()
            }
            return render(request, 'products.html', content)
        else:
            return redirect('/')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "mijozlar": Mijoz.objects.filter(ombor=request.user),
                "user": request.user.username.capitalize()
            }
            return render(request, 'clients.html', content)
        else:
            return redirect('/')
