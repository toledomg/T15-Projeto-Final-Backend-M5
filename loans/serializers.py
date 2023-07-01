from .models import Loans
from rest_framework import serializers
from loans.models import Loans


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
