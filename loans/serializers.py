from .models import Loans
from rest_framework import serializers
from users.serializers import UserSerializer


class LoansSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loans
        fields = "__all__"


class CreateLoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loans
        fields = "__all__"
        read_only_fields = [
            "id",
            "loan_initial",
            "loan_return",
            "is_returned",
            "user"
        ]

    def create(self, validated_data):
        return super().create(validated_data)


class CreateReturnSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Loans
        fields = "__all__"
        read_only_fields = [
            "id",
            "loan_initial",
            "loan_return",
            "is_returned",
            "user"
        ]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
