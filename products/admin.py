from django.contrib import admin
from .models import Category, Product, ProductSKU, ProductImage


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductSKU)
admin.site.register(ProductImage)
