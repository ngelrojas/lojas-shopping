from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models.user import User
from .models.profile import ProfileBuyer
from .models.profile import ProfileSeller
from .models.product import Product
from .models.order import Order


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_activate']
    list_filter = []
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {'fields': (
                'first_name',
                'last_name',
                'is_delete',)}),
        (
            _('Permissions'),
            {'fields': ('is_activate', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(ProfileBuyer)
admin.site.register(ProfileSeller)
admin.site.register(Product)
admin.site.register(Order)
