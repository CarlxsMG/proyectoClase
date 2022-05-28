# Third party imports
from rest_framework import viewsets

# Local imports
from .models import SellerUser, BuyerUser, ManagementUser
from .serializers import SellerSerializer, BuyerSerializer, ManagementSerializer


# Viewsets
class SellerViewSet(viewsets.ModelViewSet):
    queryset = SellerUser.objects.all()
    serializer_class = SellerSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = BuyerUser.objects.all()
    serializer_class = BuyerSerializer


class ManagementViewSet(viewsets.ModelViewSet):
    queryset = ManagementUser.objects.all()
    serializer_class = ManagementSerializer

