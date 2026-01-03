import secrets
from django.db import models
from django.contrib.auth.models import User

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=64, unique=True, editable=False)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.key:
            # Automatically generate secure key
            self.key = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

class Employes(models.Model):
    emp_id = models.IntegerField(null=False, unique=True)
    emp_name = models.CharField(max_length=100)
    disgination = models.CharField(max_length=100)


    def __str__(self):
        return self.emp_name
