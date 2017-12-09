from django.contrib import admin

# Register your models here.
from apps.product.models import ProductCategory, Product, ProductImage

admin.site.register(ProductCategory)


class ProductImageAdmin(admin.ModelAdmin) :
    list_display = ('image_tag', 'product')
    search_fields = ('product',)


admin.site.register(ProductImage, ProductImageAdmin)


class ProductAdmin(admin.ModelAdmin) :
    list_display = ('name', 'image_tag', 'show_categories', 'brand')
    search_fields = ('name', 'brand')

    def show_categories(self, obj) :
        return "\n; ".join([cat.title for cat in obj.categories.all()])

    def get_queryset(self, request) :
        return super().get_queryset(request).prefetch_related('categories')


admin.site.register(Product, ProductAdmin)
