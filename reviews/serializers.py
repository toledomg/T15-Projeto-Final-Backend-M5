from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from books.serializers import BookSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "book", "rating", "comment"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}}

    def create(self, validated_data: dict):
        return Review.objects.create(**validated_data)
