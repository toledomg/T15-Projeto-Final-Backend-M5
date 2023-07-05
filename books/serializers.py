from rest_framework import serializers

from books.models import *
from copies.models import Copy
import uuid

class CopyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = [
            "id",
            "is_available",
            "serial_number"
        ]

class BookSerializer(serializers.ModelSerializer):

    copies_count = serializers.IntegerField(write_only=True)
    copies = CopyBookSerializer(many=True)


    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "category",
            "copies_count",
            "copies"
        ]


    def create(self, validated_data):
        copies_count = validated_data.pop("copies_count")
        copies_list = []

        book = Book.objects.create(**validated_data)

        for _ in range(copies_count):
            hash_copy = str(uuid.uuid4().hex)
            copy = Copy.objects.create(serial_number=hash_copy, book=book)
            copies_list.append(copy)

        return book
       
        


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model: Follow
        fields = ["id", "book", "user"]
