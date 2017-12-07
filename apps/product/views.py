# Create your views here.
from django.views.generic import ListView, DetailView

from apps.product.models import Product


class ProductListView(ListView) :
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView) :
    model = Product
    template_name = 'product/detail.html'
    slug_field = 'slug'
