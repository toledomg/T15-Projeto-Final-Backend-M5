from django.db import models


class Copy(models.Model):
    is_available = models.BooleanField(default=True, null=True)
    serial_number = models.CharField(null=True)
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
