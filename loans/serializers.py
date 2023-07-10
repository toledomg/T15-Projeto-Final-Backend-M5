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
            "copy_id",
        ]

        extra_kwargs = {"id": {"read_only": True}, "user": {"read_only": True}}

    def create(self, validated_data):
        loan_return = timezone.now() + timedelta(days=7)

        blocking_date = validated_data.get("blocking_date")

        if blocking_date and blocking_date >= timezone.now():
            raise ValidationError("A data de bloqueio deve ser maior que a data atual")

        if loan_return.weekday() >= 5:
            loan_return += timedelta(days=7 - loan_return.weekday())

        copy_id = validated_data.pop("copy_id")
        copy = Copy.objects.get(id=copy_id)

        if not copy.is_available:
            raise ValidationError({"detail": "Não há copias disponíveis no momento"})

        copy.is_available = False
        copy.save()

        loan = Loans.objects.create(
            copy=copy, loan_return=loan_return, **validated_data
        )

        return loan
