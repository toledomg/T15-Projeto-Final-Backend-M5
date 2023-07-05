from django.shortcuts import get_object_or_404
from .models import Copy
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsLibraryCollaboratorOrOwner

from .serializers import CopySerializer
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from books.models import Book
from users.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopyBookView(ListAPIView):
    serializer_class = CopySerializer


    def get_queryset(self):
        instance_book = get_object_or_404(Book, pk=self.kwargs.get("pk"))
        queryset = Copy.objects.filter(book=instance_book)

        return queryset
