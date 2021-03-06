from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'toroto_staff',
    ]
    fieldsets = (
      (None, {
        'fields': (
          'username',
          'password',
        )
      }),
      ('Personal info', {
        'fields': (
          'first_name',
          'last_name',
          'email'
        )
      }),
      ('Role', {
        'fields': (
          'toroto_staff',
        )
      }),
      ('Permissions', {
        'fields': (
          'is_active',
          'is_staff',
          'is_superuser',
          # 'groups',
          # 'user_permissions'
          )
      }),
      # ('Important dates', {
      #   'fields': (
      #     'last_login',
      #     'date_joined'
      #   )
      # })
    )



admin.site.register(CustomUser, CustomUserAdmin)
