# Django imports
from django.db import models

# Local imports
from apps.base.user.models import BuyerUser, ManagementUser, SellerUser
from apps.base.vehicle.models import Vehicle


# Models.
class Contract(models.Model):
    """
    Class to define customs Contracts

    Inheritances:
        Model ([model]): Model class provided by django
    """

    _STATS = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('R', 'Rejected')
    ]

    code = models.CharField(max_length=20, verbose_name='Code identifier')
    status = models.CharField(max_length=1, choices=_STATS, verbose_name='Status of contract')
    fee = models.SmallIntegerField(default=2, verbose_name='Fee of management')

    seller = models.ForeignKey(SellerUser, on_delete=models.DO_NOTHING, verbose_name='Seller of vehicle')
    buyer = models.ForeignKey(BuyerUser, on_delete=models.DO_NOTHING, verbose_name='Buyer of vehicle')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING, verbose_name='Product to sell')
    manager = models.ForeignKey(ManagementUser, on_delete=models.DO_NOTHING, verbose_name='Manager')
