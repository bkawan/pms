# Create your views here.
from django.views.generic import DetailView
from django_filters.views import FilterView

from apps.company.models import CompanyDetail
from apps.product.filters import ProductFilter
from apps.product.models import Product, ProductCategory


class ProductListView(FilterView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    ordering = ('-id')

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('categories')
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        ctx['categories'] = ProductCategory.objects.all()
        ctx['brands'] = Product.objects.filter(brand__isnull=False).values_list('brand', flat=True).distinct().order_by(
            'brand')
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        return ctx

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related('categories')
        return qs
