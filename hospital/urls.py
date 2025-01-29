from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema view setup
schema_view = get_schema_view(
   openapi.Info(
      title="Hospital Management API",
      default_version='v1',
      description="API documentation for managing a hospital system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@hospital.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('management.urls')),  # Include your app's API routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),  # Swagger UI configuration
]
