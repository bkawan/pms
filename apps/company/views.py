# Create your views here.
from django.views.generic import ListView, DetailView

from apps.company.models import Client, CompanyDetail


class ClientListView(ListView) :
    model = Client
    template_name = 'company/clients.html'
    context_object_name = 'clients'

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        return ctx


class CompanyDetailView(DetailView) :
    model = CompanyDetail
    template_name = 'company/about.html'
    slug_field = 'slug'
