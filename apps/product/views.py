# Create your views here.
from django.views.generic import ListView, DetailView

from apps.company.models import CompanyDetail
from apps.product.models import Product


class ProductListView(ListView) :
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        return ctx


class ProductDetailView(DetailView) :
    model = Product
    template_name = 'product/detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        return ctx
