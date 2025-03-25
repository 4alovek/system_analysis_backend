from django.contrib import admin
from .models import AppUser

@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    search_fields = ('email', 'full_name')
