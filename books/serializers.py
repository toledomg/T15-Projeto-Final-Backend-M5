from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from books.models import *
from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "category",
            "copies_count",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
        }


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model: Follow
        fields = ["id", "book", "user"]
