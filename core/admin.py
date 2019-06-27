from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.contrib.auth.models import Group


# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'is_admin', 'is_school_staff', 'is_student', 'password')
        }),
        ('Location', {
            'fields': ['address', 'phone', 'nationality']
        }),
        ('Permisions', {
            'fields': ('is_superuser', 'is_staff')
        }),
        ('Date Info', {
            'fields': ('date_joined', 'last_login')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'is_admin', 'is_school_staff', 'is_student', 'password')
        }),
        ('Location', {
            'fields': ['address', 'phone', 'nationality']
        }),
        ('Permisions', {
            'fields': ('is_superuser', 'is_staff')
        }),
        ('Date Info', {
            'fields': ('date_joined', 'last_login')
        })
    )
    list_display = ('email', 'first_name', 'last_name', 'is_admin',
                    'is_school_staff', 'is_student', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('email',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['email']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, UserProfileAdmin)
