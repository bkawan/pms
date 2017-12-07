from django.urls import path

from apps.product.views import ProductListView, ProductDetailView

app_name = 'product'
urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail')
]
