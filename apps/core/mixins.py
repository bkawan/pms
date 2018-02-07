from apps.company.models import CompanyDetail


class CompanyDetailContextDataMixin:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['company_detail'] = CompanyDetail.objects.first()
        return ctx
