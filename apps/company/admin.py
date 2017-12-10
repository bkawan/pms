from django.contrib import admin

# Register your models here.
from apps.company.models import CompanyDetail, Service, HomePageTopImageSlider, TeamMember, Testimonial, \
    Client

admin.site.register(HomePageTopImageSlider)
admin.site.register(Testimonial)


class CompanyDetailAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'email', 'address', 'phone1', 'user')
    prepopulated_fields = {'slug':('name',)}

    # readonly_fields = ('slug',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ServiceAdmin(admin.ModelAdmin):
    fields = ['company', 'name', 'description', 'image', 'icon', 'slug']
    prepopulated_fields = {'slug':('name',)}
    autocomplete_fields = ['company']

    def has_add_permission(self, request):
        if Service.objects.count() == 4:
            return False
        return True


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'email', 'phone', 'website')


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(TeamMember, TeamMemberAdmin)

admin.site.register(Client, ClientAdmin)
admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Service, ServiceAdmin)
