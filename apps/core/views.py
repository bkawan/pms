# Create your views here.
from django.views.generic import TemplateView

from apps.company.models import CompanyDetail, HomePageTopImageSlider, Service, TeamMember, Client
from apps.product.models import Product


class LandingPageView(TemplateView) :
    template_name = 'landing.html'

    def get_context_data(self, **kwargs) :
        ctx = super().get_context_data(**kwargs)
        company = CompanyDetail.objects.first()
        ctx['company_detail'] = company
        ctx['sliders'] = HomePageTopImageSlider.objects.filter(company=company)
        ctx['services'] = Service.objects.filter(company=company)
        ctx['team_members'] = TeamMember.objects.filter(company=company)
        ctx['clients'] = Client.objects.filter(company=company)
        products = Product.objects.filter(company=company).prefetch_related('categories')
        ctx['products'] = products[:8]
        return ctx
