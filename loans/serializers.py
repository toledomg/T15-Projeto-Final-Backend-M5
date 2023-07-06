from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.dispatch import receiver

from django.db.models.signals import post_save
from datetime import timedelta
from django.utils import timezone

from loans.models import Loans
from copies.serializers import CopySerializer
from users.serializers import UserSerializer
from copies.models import Copy


class LoansSerializer(serializers.ModelSerializer):
    copy_id = serializers.IntegerField(write_only=True)
    copy = CopySerializer(read_only=True)
    user = UserSerializer

    class Meta:
        model = Loans
        fields = [
            "id",
            "loan_initial",
            "loan_return",
            "is_delay",
            "is_returned",
            "blocking_date",
            "copy",
            "user",
            "copy_id"
        ]

        extra_kwargs = {

            "id": {"read_only": True},
            "user": {"read_only": True}
        }

    def create(self, validated_data):
        loan_return = timezone.now() + timedelta(days=5)
        if loan_return.weekday() in [5, 6]:
            loan_return += timedelta(days=5 - loan_return.weekday())

        copy_id = validated_data.pop("copy_id")
        copy = Copy.objects.get(id=copy_id)
        if not copy.is_available:
            raise ValidationError("Não há copias disponíveis no momento")
        copy.is_available = False
        copy.save()
        loan = Loans.objects.create(copy=copy, loan_return=loan_return, **validated_data)

        return loan

    # def update(self, instance, validated_data):

    #     instance.loan_return = validated_data.get(
    #         'loan_return', instance.loan_return)

    #     instance.save()
    #     return instance

    # def save(self, *args, **kwargs):

    #     if not self.instance.loan_return:
    #         self.instance.loan_return = self.instance.loan_initial + timedelta(
    #             days=5)

    #         if self.instance.loan_return.weekday() in [5, 6]:
    #             self.instance.loan_return += timedelta(
    #                 days=5 - self.instance.loan_return.weekday())

    #     if self.instance.loan_return <= timezone.now():
    #         self.instance.is_delay = False
    #         # self.instance.blocking_date = timezone.now() + timedelta(days=7)

    #     if self.instance.loan_return > timezone.now():
    #         self.instance.blocking_date = timezone.now() + timedelta(days=7)
    #         self.instance.is_delay = True

    #     return super().save(*args, **kwargs)

    # def update_blocked_status(self):
    #     delay_loan_books = self.user.loans.filter(is_delay=True)
    #     if delay_loan_books.exists():
    #         self.is_active = False
    #     else:
    #         self.is_active = True
    #     self.user.update_blocked_status()



#@receiver(post_save, sender=Loans)
# def update_user_blocked_status(sender, instance, **kwargs):
 #   instance.user.update_blocked_status()
