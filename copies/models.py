from django.db import models


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    in_stock = models.BooleanField(default=True, null=True)
    copies_count = models.PositiveIntegerField(null=True)

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
