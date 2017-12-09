from django.urls import path

from apps.company.views import ClientListView, CompanyDetailView

app_name = 'company'
urlpatterns = [
    path('clients/', ClientListView.as_view(), name='clients'),
    path('about/<slug:slug>/', CompanyDetailView.as_view(), name='about'),
]
