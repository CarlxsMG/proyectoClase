#  Third party imports
from rest_framework.serializers import ModelSerializer

# Local imports 
from .models import Vehicle


# Serializers.
class VehicleSerializer(ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'