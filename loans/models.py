from django.db import models
from django.utils import timezone


class Loans(models.Model):
    class Meta:
        ordering = ["id"]
            
    loan_initial = models.DateTimeField(default=timezone.now)
    loan_return = models.DateTimeField(null=True)
    is_delay = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    blocking_date = models.DateTimeField(null=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans"
    )

    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.PROTECT, related_name="copy"
    )
