from django.shortcuts import get_object_or_404
from .models import Copy
from .serializers import CopySerializer
from rest_framework import generics
from books.models import Book

class CopyBookView(generics.ListAPIView):
    serializer_class = [CopySerializer]

    def get_queryset(self):
       queryset=super().get_queryset()
       instance_book = get_object_or_404(Book, pk=self.kwargs.get("pk"))

       return queryset.filter(book=instance_book)
