# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local imports
from .models import SellerUser, BuyerUser, ManagementUser


class SellerAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', ),
        }),
    )
    
    list_display = ('id', 'email', 'is_active',)
    list_display_links = ('id', 'email',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ['id', 'email',]

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields

class BuyerAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', ),
        }),
    )
    
    list_display = ('id', 'email', 'is_active',)
    list_display_links = ('id', 'email',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ['id', 'email',]

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields


class ManagementAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_bussines', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_staff', 'is_active', ),
        }),
    )
    
    list_display = ('id', 'email', 'is_active',)
    list_display_links = ('id', 'email',)
    list_filter = ('is_staff', 'is_active',)
    search_fields = ['id', 'email',]

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields
    

admin.site.register(SellerUser, SellerAdmin)
admin.site.register(BuyerUser, BuyerAdmin)
admin.site.register(ManagementUser, ManagementAdmin)
