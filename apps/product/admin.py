from django.contrib import admin

# Register your models here.
from apps.product.models import ProductCategory, Product, ProductImage

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
