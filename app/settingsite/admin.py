from django.contrib import admin

# Register your models here.
from .models import Manzil, BizHaqimizda

@admin.register(Manzil)
class AdminSite(admin.ModelAdmin):
    list_display = ["id", 'joylashov','tel_number', 'email']
    list_editable = ['joylashov','tel_number', 'email']

@admin.register(BizHaqimizda)
class AdminSite(admin.ModelAdmin):
    list_display = ["id", 'body']
    list_editable = ['body']