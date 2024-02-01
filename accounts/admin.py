# allfiles/admins.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email', 'rank', 'firstname', 'lastname', 'is_admin', 'last_login']
    list_filter = ('is_admin', 'is_staff')  # แก้ไขเป็น 'is_staff' แทน 'is_active'
    readonly_fields = ('last_login',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('rank', 'firstname', 'lastname')}),
        (_('Permissions'), {'fields': ('is_admin', 'is_staff', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        (_('Personal Info'), {'fields': ('rank', 'firstname', 'lastname')}),
        (_('Permissions'), {'fields': ('is_admin', 'is_staff', 'groups', 'user_permissions')}),
    )

admin.site.register(User, UserAdmin)
