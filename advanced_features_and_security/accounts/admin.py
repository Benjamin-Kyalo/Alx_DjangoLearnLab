from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Custom admin for our CustomUser model
# We extend Django's built-in UserAdmin but add our extra fields (date_of_birth, profile_photo).
class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin user list
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

    # Fields you can filter users by
    list_filter = ("is_staff", "is_superuser", "is_active")

    # How the form is structured when editing a user
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields when creating a new user from admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)


# Register the model + custom admin
admin.site.register(CustomUser, CustomUserAdmin)
