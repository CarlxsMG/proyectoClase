# Django imports
from django.urls import path, include

# Third party imports
from rest_framework.routers import DefaultRouter

# Local imports
from .viewsets import PaymentViewSet

# Creation of the router and register the viewsets
router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment-viewset')

# List of urls
urlpatterns = [
    path('api/payment/', include(router.urls), name='payments-viewset')
]