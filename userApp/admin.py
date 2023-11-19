from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class OmborAdmin(UserAdmin):
    model = Ombor
    fieldsets = UserAdmin.fieldsets + (
        ('Ombor ustunlari', {
            'fields': ('ism', 'nom', "soha", "tel", "manzil")
        }),
    )
    list_display = ['id', 'username', 'ism', 'nom', 'soha', 'tel', 'manzil', 'is_staff', 'is_active']


admin.site.register(Ombor, OmborAdmin)
