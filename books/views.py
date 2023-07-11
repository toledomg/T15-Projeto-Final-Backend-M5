from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Book, Follow
from .serializers import BookSerializer, FollowSerializer, FollowedBooksSerializer
from rest_framework.exceptions import ValidationError


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class FollowCreateView(CreateAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.request.data.get("book_id")
        book = Book.objects.get(id=book_id)
        existing_follow = Follow.objects.filter(user=self.request.user, book=book)
        if existing_follow.exists():
            raise ValidationError("You already follow this book")
        serializer.save(user=self.request.user, book=book)


class FollowedBooksListView(ListAPIView):
    serializer_class = FollowedBooksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)
