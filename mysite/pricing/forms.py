from django import forms
from .models import PricingConfiguration

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = ['param_name', 'is_active']
