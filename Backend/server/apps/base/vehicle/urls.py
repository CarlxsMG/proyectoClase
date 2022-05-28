# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import VehicleViewSet

# Creation of the router and register the viewsets
router = DefaultRouter()
router.register(r'', VehicleViewSet, basename='vehicle-viewset')

# List of urls
urlpatterns = [
    path('api/vehicle/', include(router.urls), name='vehicles-viewset')
]