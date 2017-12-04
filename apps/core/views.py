# Create your views here.
from django.views.generic import TemplateView

from apps.company.models import CompanyDetail


class LandingPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()

        return ctx
