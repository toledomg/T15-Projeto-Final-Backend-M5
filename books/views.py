from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, Request, status
from .models import Book, Follow
from .serializers import BookSerializer, FollowSerializer, FollowedBooksSerializer
from django.core.mail import send_mail
from django.conf import settings


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


class EmailNotificationView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        user = request.user
        book_id = request.data.get("book_id")

        try:
            follow = Follow.objects.get(user=user, book_id=book_id)
            book = follow.book

            copies = book.copies.all()
            available_copies = copies.filter(is_available=True)

            if available_copies.exists():
                subject = "Notificação de Disponibilidade do Livro"
                message = f"O livro {book.title} está agora disponível para empréstimo. Faça o seu pedido!"
                recipient_list = [user.email]

                send_mail(
                    subject,
                    message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=recipient_list,
                )
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Follow.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
