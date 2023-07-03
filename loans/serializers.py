from .models import Loans
from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"

    def create(self, validated_data):
        loan = Loans.objects.create(**validated_data)
        return loan

    def update(self, instance, validated_data):
        instance.return_date = validated_data.get(
            'loan_return', instance.loan_return)
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        if not self.loan_return:
            self.loan_return = self.loan_initial + timedelta(days=5)
            if self.loan_return.weekday() in [5, 6]:
                self.loan_return += timedelta(
                    days=5 - self.loan_return.weekday())

        if self.loan_return <= timezone.now():
            self.is_delay = False
            # self.blocking_date = timezone.now() + timedelta(days=7)

        if self.loan_return > timezone.now():
            self.blocking_date = timezone.now() + timedelta(days=7)
            self.is_delay = True

        super().save(*args, **kwargs)


def update_blocked_status(self):
        delay_loan_books = self.Loans_set.filter(is_delay=True)

        if delay_loan_books.exists():
            self.is_active = False
        else:
            self.is_active = True

        self.user.update_blocked_status()  

@receiver(post_save, sender=Loans)
def update_user_blocked_status(sender, instance, **kwargs):
    instance.user.update_blocked_status()



