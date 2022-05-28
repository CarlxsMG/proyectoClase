#  Third party imports
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

# Local imports 
from .models import Payment


# Serializers.
class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'