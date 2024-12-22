from django.contrib import admin
from django.utils.html import format_html
from .models import User, Unit, UserRole, Role, RolePermission

admin.site.site_header = 'Powerint User Management'
admin.site.site_title = 'Powerint User Management'

class UserAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'unit__name')
    search_fields = ('name', 'email', 'unit__name')
    list_filter = ['unit']
    autocomplete_fields = ['unit']
    ordering = ['name', 'unit__name']

    def password_field(self, obj):
        if obj:
            return format_html('<a class="button" href="/powerint/change-password/{}/">Reset Password</a>', obj.id)
        return "-"

    readonly_fields = ['password_field']
    fields = ['name', 'email', 'unit', 'password_field']

    def get_exclude(self, request, obj=None):
        excluded = super().get_exclude(request, obj) or []
        if not request.user.is_superuser:
            return excluded + ['password']
        return excluded    

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent__name')
    search_fields = ('name', 'parent__name')
    list_filter = ['parent']
    autocomplete_fields = ['parent']
    ordering = ['name', 'parent__name']

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user__name', 'role')
    search_fields = ('user__name', 'role')
    list_filter = ['role']
    autocomplete_fields = ['user']
    ordering = ['user__name', 'role']

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ['name']

class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role__name', 'permission')
    search_fields = ('role__name', 'permission')
    list_filter = ['role']
    autocomplete_fields = ['role']
    ordering = ['role__name', 'permission']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(RolePermission, RolePermissionAdmin)