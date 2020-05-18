from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_filter = ("is_admin",)
    list_display = ["email", "name", "phone_number"]
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_admin", "is_superuser",)}),
        (_("Important Dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "phone_number", "password1", "password2"),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
