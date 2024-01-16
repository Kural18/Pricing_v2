# pricing_api/urls.py
from django.urls import path
from .views import CalculatePricing

app_name = 'pricing_api'

urlpatterns = [
    path('calculate_pricing/', CalculatePricing.as_view(), name='calculate_pricing'),
]
