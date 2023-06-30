from django.db import models


class Copy(models.Model):
    in_stock = models.BooleanField(default=True, null=True)
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
