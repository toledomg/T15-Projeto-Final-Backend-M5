from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    library_collaborator = models.BooleanField(default=False)
    have_permission = models.DateField(default=None, blank=True, null=True)
