from django.contrib import admin

# Register your models here.
from apps.company.models import CompanyDetail, Service, HomePageTopImageSlider, TeamMember, Testimonial, \
    Client

admin.site.register(CompanyDetail)
admin.site.register(Service)
admin.site.register(HomePageTopImageSlider)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Client)
