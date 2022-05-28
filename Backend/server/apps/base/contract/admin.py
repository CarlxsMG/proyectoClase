# Django imports
from django.contrib import admin

# Local imports
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'code','status','seller','buyer','vehicle','manager',)
    list_display_links = ('id', 'vehicle', 'seller', 'buyer', 'manager',)
    list_filter = ('status',)
    search_fields = ['code', 'fee']


admin.site.register(Contract, ContractAdmin)
