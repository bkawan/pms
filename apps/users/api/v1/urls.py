from rest_framework.routers import DefaultRouter

from apps.users.api.v1.views import UserViewSet

app_name = 'v1'

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = router.urls
