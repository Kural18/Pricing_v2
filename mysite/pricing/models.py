from django.db import models
from django.contrib.auth.models import User

class PricingConfiguration(models.Model):
    param_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='configurations_created')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='configurations_modified')
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.param_name
