from django.http import Http404
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
                "user": request.user.username.capitalize(),
                "nom": request.user.nom.capitalize(),
                "rasm": request.user.rasm,
                "logo": request.user.logo
            }
            return render(request, 'products.html', content)
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom=request.POST.get("pr_name"),
                brend=request.POST.get("pr_brand"),
                olchov=request.POST.get("pr_measure"),
                narx=request.POST.get("pr_price"),
                miqdor=request.POST.get("pr_amount"),
                kelgan_sana=request.POST.get("pr_date"),
                ombor=request.user
            )
            return redirect('/asosiy/mahsulotlar/')
        else:
            return redirect('/')


class UpdateMahsulot(View):
    def get(self, request, num):
        if request.user.is_authenticated:
            context = {
                "mahsulot": Mahsulot.objects.get(id=num)
            }
            return render(request, 'product_update.html', context)
        else:
            return redirect('/')

    def post(self, request, num):
        if request.user.is_authenticated:
            Mahsulot.objects.filter(id=num).update(
                nom=request.POST.get("name"),
                brend=request.POST.get("brand_name"),
                narx=request.POST.get("price"),
                miqdor=request.POST.get("amount"),
                olchov=request.POST.get("measure"),
                kelgan_sana=request.POST.get("date"),
            )
            return redirect("/asosiy/mahsulotlar/")
        else:
            return redirect('/')


class DeleteMahsulot(View):
    def get(self, request, num):
        if request.user.is_authenticated:
            Mahsulot.objects.get(id=num).delete()
            return redirect('/asosiy/mahsulotlar/')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "mijozlar": Mijoz.objects.filter(ombor=request.user),
                "user": request.user.username.capitalize(),
                "nom": request.user.nom.capitalize(),
                "rasm": request.user.rasm,
                "logo": request.user.logo
            }
            return render(request, 'clients.html', content)
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('client_name'),
                nom=request.POST.get('client_shop'),
                manzil=request.POST.get('client_address'),
                tel=request.POST.get('client_phone'),
                qarz=request.POST.get('client_debt'),
                ombor=request.user
            )
            return redirect('/asosiy/mijozlar/')
        else:
            return redirect('/')


class UpdateMijoz(View):
    def get(self, request, num):
        if request.user.is_authenticated:
            context = {
                "mijoz": Mijoz.objects.get(id=num)
            }
            return render(request, 'client_update.html', context)
        else:
            return redirect('/')

    def post(self, request, num):
        if request.user.is_authenticated:
            Mijoz.objects.filter(id=num).update(
                ism=request.POST.get("client_name"),
                nom=request.POST.get("client_shop"),
                manzil=request.POST.get("client_phone"),
                tel=request.POST.get("client_address"),
                qarz=request.POST.get("client_debt"),
                ombor=request.user
            )
            return redirect("/asosiy/mijozlar/")
        else:
            return redirect('/')


class DeleteMijoz(View):
    def get(self, request, num):
        if request.user.is_authenticated:
            Mijoz.objects.get(id=num).delete()
            return redirect('/asosiy/mijozlar/')
