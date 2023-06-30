from django.db import models
from time import strftime
from datetime import datetime, timedelta


def loan_return():
    return datetime.now() + timedelta(days=10)


class Loans(models.Model):
    loan_initial = models.DateTimeField(auto_now_add=True)
    loan_return = models.DateTimeField(default=loan_return)
    is_returned = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans"
    )

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        related_name="book"
    )
