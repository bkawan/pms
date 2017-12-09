from django.contrib import admin

# Register your models here.
from apps.company.models import CompanyDetail, Service, HomePageTopImageSlider, TeamMember, Testimonial, \
    Client

admin.site.register(HomePageTopImageSlider)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(Client)


class CompanyDetailAdmin(admin.ModelAdmin) :
    list_display = ('name', 'email', 'address', 'phone1', 'user')
    prepopulated_fields = {'slug' : ('name',)}

    # readonly_fields = ('slug',)

    def has_add_permission(self, request) :
        return False

    def has_delete_permission(self, request, obj=None) :
        return False


class ServiceAdmin(admin.ModelAdmin) :
    def has_add_permission(self, request) :
        if Service.objects.count() == 4 :
            return False
        return True


admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Service, ServiceAdmin)
