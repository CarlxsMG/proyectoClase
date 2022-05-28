# Django imports
from django.contrib import admin

# Local imports
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'type', 'status','amount','contract',)
    list_display_links = ('id', 'contract', )
    list_filter = ('status', 'type',)
    search_fields = ['amount',]


admin.site.register(Payment, PaymentAdmin)
