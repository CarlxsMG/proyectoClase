#  Third party imports
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

# Local imports 
from .models import Vehicle


# Serializers.
class VehicleSerializer(ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'