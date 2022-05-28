#  Third party imports
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

# Local imports 
from .models import Contract


# Serializers.
class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'