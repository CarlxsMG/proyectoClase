# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Vehicle
from .serializers import VehicleSerializer

# Viewsets
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


