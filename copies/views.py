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


class CopyBookView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    serializer_class = [CopySerializer]

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_book = get_object_or_404(Book, pk=self.kwargs.get("pk"))

        return queryset.filter(book=instance_book)
