from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import IsLibraryCollaboratorOrOwner
from books.models import Book
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        instance_book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        queryset = Review.objects.filter(book=instance_book)

        return queryset


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "pk"
