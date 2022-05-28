# Django imports
from django.contrib import admin

# Local imports
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'brand','model','status','price','plate','owner',)
    list_display_links = ('id', 'owner',)
    list_filter = ('status',)
    search_fields = ['brand', 'model','price','plate','owner',]


admin.site.register(Vehicle, VehicleAdmin)
