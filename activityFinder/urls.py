from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^activity/', include('apps.activity.urls')),
    url(r'^location/', include('apps.location.urls')),
]
