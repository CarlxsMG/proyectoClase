from django.db import models

from Backend.server.apps.base.user.models import BuyerUser, ManagementUser, SellerUser
from Backend.server.apps.base.vehicle.models import Vehicle

# Create your models here.
class Contract(models.Model):
    """
    Class to define customs Vehicles

    Inheritances:
        Model ([model]): Model class provided by django
    """

    _STATS = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('R', 'Rejected')
    ]

    code = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=_STATS)
    fee = models.IntegerField(max_length=2, default=2)

    seller = models.ForeignKey(SellerUser, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(BuyerUser, on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(ManagementUser, on_delete=models.DO_NOTHING)
