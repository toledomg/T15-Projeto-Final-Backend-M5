from django.db import models


class Copy(models.Model):
    in_stock = models.BooleanField(default=True, null=True)
    copies_count = models.PositiveIntegerField(null=True)

    is_available = models.BooleanField(default=True, null=True)
    serial_number = models.CharField(null=True)

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
