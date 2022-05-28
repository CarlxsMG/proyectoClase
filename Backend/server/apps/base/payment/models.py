# Django imports
from django.db import models

# Local imports
from apps.base.contract.models import Contract


# Models.
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

    type = models.CharField(max_length=1, choices=_TYPES, verbose_name='Type of payment')
    status = models.CharField(max_length=1, choices=_STATS, verbose_name='Status of payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Amount to pay')
    
    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING, verbose_name='Contract referer')