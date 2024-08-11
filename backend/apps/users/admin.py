from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]
    list_display = (
        "username", "email", "first_name",
        "last_name", "is_staff", 'is_verified', 'is_active',)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    'is_verified',
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('email', "username", "password1", "password2"),
            },
        ),
    )
    list_filter = (
        'is_verified', "is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
