from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from books.models import *


class BookSerializer(serializers.ModelSerializer):
    def create(self, validate_data: dict) -> Book:
        return Book.objects.all(**validate_data)

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
        extra_kwargs = {"copies_count": {"read_only": True}}


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model: Follow
        fields = ["id", "book", "user"]
