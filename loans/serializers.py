from .models import Loans
from rest_framework import serializers
from users.serializers import UserSerializer
from users.models import User
from loans.models import Loans


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

    # def create(self, validated_data):
    #     book_data = validated_data.pop("book_id")
    #     user = validated_data["user"]
    #     loan = Loans.objects.create(**validated_data, book_id=book)

    #     User.objects.filter(email=user).update(is_debt="True")

    #     return loan

    # def update(self, instance, validated_data):
    #     loan = 
