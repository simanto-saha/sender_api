from django.contrib import admin
from .models import Employes
from .models import APIKey
from django.utils.html import format_html

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_key', 'user', 'is_active', 'created_at', 'last_used']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'key', 'user__username']
    readonly_fields = ['key', 'created_at', 'last_used', 'display_full_key']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('user', 'name', 'is_active')
        }),
        ('API Key Details', {
            'fields': ('display_full_key', 'created_at', 'last_used'),
            'description': 'API key automatically generated হবে। Copy করে রাখুন!'
        }),
    )
    
    def display_key(self, obj):
        """List view তে partial key দেখাবে"""
        return format_html(
            '<code style="background: #f4f4f4; padding: 5px;">{}</code>',
            f"{obj.key[:15]}...{obj.key[-5:]}"
        )
    display_key.short_description = 'API Key'
    
    def display_full_key(self, obj):
        """Detail view তে full key দেখাবে"""
        if obj.key:
            return format_html(
                '<div>'
                '<strong> Your API Key:</strong><br><br>'
                '<code>{}</code>'
                '</div>',
                obj.key
            )
        return "Key will be generated after save"
    display_full_key.short_description = 'Full API Key'
    
    def save_model(self, request, obj, form, change):
        """Save করার সময় message দেখাবে"""
        super().save_model(request, obj, form, change)
        if not change:  # নতুন key হলে
            self.message_user(
                request,
                f'✅ API Key "{obj.name}" successfully created! Key: {obj.key}'
            )



admin.site.register(Employes)
