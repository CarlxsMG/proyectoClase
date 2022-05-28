# Third party imports
from rest_framework import viewsets

# Local imports
from .models import Payment
from .serializers import PaymentSerializer


# Viewsets
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


