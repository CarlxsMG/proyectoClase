#  Third party imports
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

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

class LoginSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)