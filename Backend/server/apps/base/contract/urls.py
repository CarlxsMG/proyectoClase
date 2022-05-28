# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import ContractViewSet

# Creation of the router and register the viewsets
router = DefaultRouter()
router.register(r'', ContractViewSet, basename='contract-viewset')

# List of urls
urlpatterns = [
    path('api/contract/', include(router.urls), name='contracts-viewset')
]