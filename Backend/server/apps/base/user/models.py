# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """
    Class to define customs Users

    Inheritances:
        User ([model]): User class provided by django
    """

    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Prefix+Phone Number")
    location = models.CharField(max_length=140, null=True, blank=True, verbose_name="Address")
    postal_code = models.IntegerField(null=True, blank=True, verbose_name="Postal Code")
    doc_identifier = models.CharField(max_length=40, null=True, blank=True, verbose_name="Document Identifier")
    bank = models.CharField(max_length=80, null=True, blank=True, verbose_name="Bank account")

    class Meta:
        abstract = True

        
class SellerUser(CustomUser):
    """
    Class to define Sellers

    Inheritances:
        CustomUser ([model]): Custom User class defined
    """

    # vehicle = models.ForeignKey(Vehicle, null=True, blank=True)
    # contract = models.ForeignKey(Contract, null=True, blank=True)

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

class BuyerUser(CustomUser):
    """
    Class to define Buyer

    Inheritances:
        CustomUser ([model]): Custom User class defined
    """

    # contract = models.ForeignKey(Contract, null=True, blank=True)

    class Meta:
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'

class ManagementUser(CustomUser):
    """
    Class to define ManagementUser

    Inheritances:
        CustomUser ([model]): Custom User class defined
    """

    id_bussines = models.CharField(max_length=100, null=True, blank=True, verbose_name="Bussines identification")

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'