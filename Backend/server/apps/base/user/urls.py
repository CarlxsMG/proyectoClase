# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import SellerViewSet, BuyerViewSet, ManagementViewSet


# Creation of the router and register the viewsets
router = DefaultRouter()
router.register(r'seller', SellerViewSet, basename='user-seller-viewset')
router.register(r'buyer', BuyerViewSet, basename='user-buyer-viewset')
router.register(r'manager', ManagementViewSet, basename='user-manager-viewset')

# List of urls
urlpatterns = [
    path('api/users/', include(router.urls), name='users-viewset')
]