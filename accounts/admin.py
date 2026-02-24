from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Changes the admin create and edit pages so that it adds the date of birth field."""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "date_of_birth",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (("Date of Birth", {"fields": ("date_of_birth",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("date_of_birth",)}),)

admin.site.register(CustomUser, CustomUserAdmin)