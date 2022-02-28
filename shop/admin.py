from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields=['name', 'description','image','price', 'quantity']

admin.site.register(Product)
# Register your models here.
