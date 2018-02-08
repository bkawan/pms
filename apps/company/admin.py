from django.contrib import admin
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from apps.company.models import CompanyDetail, Service, HomePageTopImageSlider, TeamMember, Client


class HomePageTopImageSliderAdmin(admin.ModelAdmin):
    exclude = ('company',)
    list_display = ['image_tag']


admin.site.register(HomePageTopImageSlider, HomePageTopImageSliderAdmin)


# admin.site.register(Testimonial)


class CompanyDetailAdmin(SummernoteModelAdmin):
    summer_note_fields = '__all__'
    search_fields = ['name']
    list_display = ('name', 'email', 'address', 'phone1', 'user')
    exclude = ('slug',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ServiceAdmin(admin.ModelAdmin):
    exclude = ('slug', 'company')

    def has_add_permission(self, request):
        if Service.objects.count() == 4:
            return False
        return True


class ClientAdmin(admin.ModelAdmin):
    exclude = ('company',)
    list_display = ('name', 'image_tag', 'email', 'phone', 'website')


class TeamMemberAdmin(admin.ModelAdmin):
    exclude = ('company',)
    list_display = ('name', 'email', 'phone')


admin.site.register(TeamMember, TeamMemberAdmin)

admin.site.register(Client, ClientAdmin)
admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Service, ServiceAdmin)
