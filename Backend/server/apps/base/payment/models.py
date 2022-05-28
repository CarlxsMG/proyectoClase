# Django imports
from django.db import models

# Local imports
from apps.base.contract.models import Contract

# Create your models here.
class Payment(models.Model):
    """
    Class to define customs Payments

    Inheritances:
        Model ([model]): Model class provided by django
    """

    _TYPES = [
        ('S', 'Sell'),
        ('F', 'Fee')
    ]

    _STATS = [
        ('P', 'Pending'),
        ('C', 'Completed')
    ]

    type = models.CharField(max_length=1, choices=_TYPES)
    status = models.CharField(max_length=1, choices=_STATS)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)