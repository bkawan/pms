from apps.company.models import CompanyDetail


def company(request):
    """ Company."""

    company = CompanyDetail.objects.last()
    return {'company_detail':company}
