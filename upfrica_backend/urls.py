from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from upfrica_backend.views import HelpCategoryViewSet, HelpArticleViewSet
from upfrica_backend.upload_image import upload_image  # ✅ custom image upload view

# Set up the API router
router = DefaultRouter()
router.register(r'categories', HelpCategoryViewSet)
router.register(r'articles', HelpArticleViewSet)

# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/help-center/', include(router.urls)),
    path('api/upload-image/', upload_image),  # ✅ image upload endpoint
]

# Serve media files in development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)