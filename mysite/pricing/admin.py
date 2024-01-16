from django.contrib import admin
from .models import PricingConfiguration

class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = ('param_name', 'is_active', 'created_by', 'created_at', 'modified_by', 'modified_at')
    search_fields = ['param_name']
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Object is being created
            obj.created_by = request.user
        obj.modified_by = request.user

        super().save_model(request, obj, form, change)

admin.site.register(PricingConfiguration, PricingConfigurationAdmin)
