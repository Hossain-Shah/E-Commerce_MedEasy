#importing libraries
from django.contrib import admin

from Shopping_Cart.models import Product
from Shopping_Cart.models import Customer

#Admin panel view for products
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "stock",
        "customer",
    )
    search_fields = ("name", "customer", "stock")
    list_filter = ("name", "customer", "availability")
    ordering = ("name",)

#Admin panel view for customers
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name", 
        "review"
    )
    list_filter = ("id", "name", "review")
    search_fields = ("id", "name", "review")
    ordering = ("id", "name", "review")


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
