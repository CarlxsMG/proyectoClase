# Django imports
from django.db import models

# Django imports
from apps.base.user.models import SellerUser


# Create your models here.
class Vehicle(models.Model):
    """
    Class to define customs Vehicles

    Inheritances:
        Model ([model]): Model class provided by django
    """

    _STATS = [
        ('A', 'Available'),
        ('R', 'Reserved'),
        ('S', 'Selled'),
        ('L', 'Locked')
    ]

    brand = models.CharField(max_length=30, null=True, blank=True, verbose_name="Brand")
    model = models.CharField(max_length=30, null=True, blank=True, verbose_name="Model")
    status = models.CharField(max_length=10, choices=_STATS, null=True, blank=True, verbose_name="Status")
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, verbose_name="Price")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    plate = models.CharField(max_length=20, null=True, blank=True, verbose_name="Plate identifier of vehicle")

    owner = models.ForeignKey(SellerUser, on_delete=models.DO_NOTHING, verbose_name="Owner")
