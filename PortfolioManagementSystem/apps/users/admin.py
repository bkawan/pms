from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group

from apps.users.models import User

admin.site.register(User)
# admin.site.unregister(Group)
