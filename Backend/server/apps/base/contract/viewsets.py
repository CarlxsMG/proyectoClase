# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Contract
from .serializers import ContractSerializer


# Viewsets
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


