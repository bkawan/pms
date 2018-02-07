# Create your views here.
from django.views.generic import ListView, DetailView

from apps.company.models import Client, CompanyDetail
from apps.core.mixins import CompanyDetailContextDataMixin


class ClientListView(CompanyDetailContextDataMixin, ListView):
    model = Client
    template_name = 'company/clients.html'
    context_object_name = 'clients'


class CompanyDetailView(CompanyDetailContextDataMixin, DetailView):
    model = CompanyDetail
    template_name = 'company/about.html'
    slug_field = 'slug'
