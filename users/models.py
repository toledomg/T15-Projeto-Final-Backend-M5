from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)

    is_superuser = models.BooleanField(default=False, null=True)
