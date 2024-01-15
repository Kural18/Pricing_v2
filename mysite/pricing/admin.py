from django.contrib import admin
from .models import PricingConfiguration

class PricingConfigurationAdmin(admin.ModelAdmin):
    list_display = ('param_name', 'is_active', 'created_by', 'created_at', 'modified_by', 'modified_at')
    search_fields = ['param_name']

admin.site.register(PricingConfiguration, PricingConfigurationAdmin)
