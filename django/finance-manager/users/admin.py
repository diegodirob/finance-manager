from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import UserChangeForm, UserCreationForm
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff',
                'is_active', 'groups', 'user_permissions'
            )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
