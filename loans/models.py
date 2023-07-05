from django.db import models
from django.utils import timezone
from datetime import timedelta


class Loans(models.Model):
    loan_initial = models.DateTimeField(auto_now_add=True)
    loan_return = models.DateTimeField(timezone.now() + timedelta(days=7))
    is_delay = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    blocking_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans"
    )

    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.PROTECT, related_name="loans"
    )
