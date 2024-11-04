from django.contrib import admin
from django.urls import path, include

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.endpoints.urls')),  # Include endpoints with the correct base path
]

# No need to add `endpoints_urlpatterns` separately; it's included above.
