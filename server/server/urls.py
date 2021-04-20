from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# Handles MEDIA URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
