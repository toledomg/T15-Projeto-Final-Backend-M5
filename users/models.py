from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True)
    collaborator = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)
    is_allowed = models.BooleanField(default=True, null=True)
