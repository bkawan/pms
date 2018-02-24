from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.forms import forms
from django.utils.translation import ugettext_lazy as _

from apps.users.models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username':'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
                    ('User Profile', {'fields':['title', 'full_name', 'image', 'gender', ]}),
                    # ('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser')}),
                ) + (
                    (None, {'fields':('username', 'password')}),
                    (_('Personal info'), {'fields':('first_name', 'last_name', 'email')}),
                    (_('Permissions'), {'fields':('is_active', 'is_staff', 'is_superuser')}),
                    # (_('Important dates'), {'fields':('last_login', 'date_joined')}),
                )
    list_display = ('id', 'username', 'full_name', 'is_superuser')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if User.objects.all().count() == 5:
            return False
        return True


admin.site.unregister(Group)
