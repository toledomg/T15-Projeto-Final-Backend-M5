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
        book_title = self.request.data.get("title")
        book = Book.objects.get(title=book_title)
        serializer.save(user=self.request.user, book=book)


class FollowedBooksListView(ListAPIView):
    serializer_class = FollowedBooksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)
