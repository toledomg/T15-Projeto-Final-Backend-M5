from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Loans(models.Model):
    loan_initial = models.DateTimeField(default=timezone.now)
    loan_return = models.DateTimeField(null=True, blank=True)
    is_delay = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    blocking_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans"
    )

    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.PROTECT,
        related_name="copy"
    )

    def save(self, *args, **kwargs):
        if not self.loan_return:
            self.loan_return = self.loan_initial + timedelta(days=5)
            if self.loan_return.weekday() in [5, 6]:
                self.loan_return += timedelta(
                    days=5 - self.loan_return.weekday())

        if self.loan_returne and self.loan_returne < timezone.now():
            self.is_delay = True
            self.blocking_date = timezone.now() + timedelta(days=7)

        if self.is_returned:
            self.blocking_date = timezone.now() + timedelta(days=7)
            self.is_delay = True

        super().save(*args, **kwargs)

        self.user.update_blocked_status()


@receiver(post_save, sender=Loans)
def update_user_blocked_status(sender, instance, **kwargs):
    instance.user.update_blocked_status()

#  Alexsandro aqui estara chamando a função para fazer o updated do is_active
# na tabela do usuario
#       a função precisa ser algo assim:
#
#       class User(AbstractUser):
#           is_active = models.BooleanField(default=False)

#     def update_blocked_status(self): (exemplo de nome da função)
#         delay_loan_books = self.Loans_set.filter(is_delay=True)

#         if delay_loan_books.exists():
#             self.is_active = False
#         else:
#             self.is_active = True

#         self.save()
