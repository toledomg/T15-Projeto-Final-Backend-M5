from django.db import models
from users.serializers import User


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    pages = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=150)
    copies_count = models.IntegerField(default=1)


class Follow(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book", null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True
    )
