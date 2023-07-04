from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer

    class Meta:
        model = Copy
        fields = ["id", "copies_count", "in_stock", "book"]

        extra_kwargs = {"id": {"read_only": True}, "book": {"read_only": True}}

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
