import django_filters

from apps.product.models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name='categories__title', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name', 'category', 'brand']
