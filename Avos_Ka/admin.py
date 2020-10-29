from django.contrib import admin
from .models import ProductList, Product, Measurment, Amount, Recepie


@admin.register(Measurment)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ["display_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("display_name", "display_measure")


@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('display_title', 'display_product_list')


@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('display_product_list_title', 'display_product_name', 'display_amount', 'display_product_measure')


@admin.register(Recepie)
class RecepieAdmin(admin.ModelAdmin):
    list_display = ('display_author', 'display_title', 'display_recepie_products', 'display_describe')
