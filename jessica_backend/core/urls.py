"""
URL configuration for core project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirect root URL to /gallery/
    path('', RedirectView.as_view(url='/gallery/', permanent=False)),

    # Include all URLs from the pageant app
    path('', include('pageant.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
