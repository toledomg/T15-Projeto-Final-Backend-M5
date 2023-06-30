from django.shortcuts import get_object_or_404
from .serializers import CopySerializer
from books.models import Book
from rest_framework import generics


class CopyBookView(generics.ListAPIView):
    serializer_class = CopySerializer

    def get_queryset(self):
        queryset =  super().get_queryset()
        instance_book = get_object_or_404(Book, pk=self.kwargs.get("pk"))

        return queryset.filter(book=instance_book)


