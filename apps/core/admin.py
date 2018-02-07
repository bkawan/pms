from django.contrib import admin

# Register your models here.
from apps.core.models import TagLine


class TagLineAdmin(admin.ModelAdmin):
    list_display = ['company_detail', 'service', 'client', 'product', 'team_member']

    def has_add_permission(self, request):
        if TagLine.objects.count() == 1:
            return False
        return True


admin.site.register(TagLine, TagLineAdmin)
