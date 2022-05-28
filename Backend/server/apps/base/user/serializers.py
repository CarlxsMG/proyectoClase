#  Third party imports
from rest_framework.serializers import ModelSerializer

# Local imports 
from .models import SellerUser, BuyerUser, ManagementUser


# Serializers.
class SellerSerializer(ModelSerializer):

    class Meta:
        model = SellerUser
        exclude = ['password', 'is_superuser', 'is_staff']

class BuyerSerializer(ModelSerializer):

    class Meta:
        model = BuyerUser
        exclude = ['password', 'is_superuser', 'is_staff']

class ManagementSerializer(ModelSerializer):

    class Meta:
        model = ManagementUser
        exclude = ['password', 'is_superuser', 'is_staff']