from django.db import models

from api.models import User


class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    security_key = models.CharField(max_length=6, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
