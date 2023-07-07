from rest_framework import serializers
from users.serializers import UserSerializer
from books.models import Book, Follow
from copies.models import Copy
import uuid


class BookSerializer(serializers.ModelSerializer):
    copies_count = serializers.IntegerField(write_only=True)
    copies = CopyBookSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "category",
            "copies_count",
            "copies",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
        }


class FollowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "book", "user"]


class FollowedBooksSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "book"]
