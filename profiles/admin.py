from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created']