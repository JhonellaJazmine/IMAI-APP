from django.contrib import admin
from .models import Category, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("barcode", "name", "price", "category", "brand", "stock_quantity", "units_sold")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)

