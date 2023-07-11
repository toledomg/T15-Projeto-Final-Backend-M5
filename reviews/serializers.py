from rest_framework import serializers
from .models import Review
from users.serializers import ReviewUserSerializer
from books.serializers import ReviewBooksSerializer
from books.models import Book


class ReviewSerializer(serializers.ModelSerializer):
    user = ReviewUserSerializer(read_only=True)
    book = ReviewBooksSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user", "book", "rating", "comment", "created_at"]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}}

    def get_user(self, obj):
        return self.context["request"].user

    def create(self, validated_data):
        user = self.context["request"].user
        book_id = self.initial_data.get("book_id")
        existing_review = Review.objects.filter(user=user, book=book_id).filter()

        if existing_review:
            raise serializers.ValidationError(
                {"error": "User already has rating for this book"}
            )
        else:
            if book_id:
                try:
                    book = Book.objects.get(id=book_id)
                    return Review.objects.create(book=book, user=user, **validated_data)
                except Book.DoesNotExist:
                    raise serializers.ValidationError({"error": "Invalid book ID"})
            else:
                raise serializers.ValidationError({"error": "Book ID is required"})
