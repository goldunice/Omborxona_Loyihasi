from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Mahsulot)
class MahsulotAdmin(ModelAdmin):
    list_display = ['id', 'ombor', 'nom', 'brend', 'olchov', 'narx', 'miqdor', 'kelgan_sana']
    list_display_links = ['id', 'nom']
    list_filter = ['ombor', 'kelgan_sana']
    search_fields = ['nom', 'brend']


@admin.register(Mijoz)
class MijozAdmin(ModelAdmin):
    list_display = ['id', 'ism', 'nom', 'manzil', 'tel', 'qarz', 'ombor']
    list_display_links = ['id', 'ism']
    list_filter = ['ombor']
    search_fields = ['ism', 'nom']
