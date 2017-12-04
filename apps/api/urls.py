from django.conf.urls import url, include

app_name = 'api'

urlpatterns = [
    url(r'^v1/', include(
        [
            url(r'^', include('apps.users.api.v1.urls'), name='user')
        ],
    ), name='v1')
]
