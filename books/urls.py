from django.urls import path
from .views import (
    BookView,
    BookDetailView,
    FollowCreateView,
    FollowedBooksListView,
    EmailNotificationView,
)

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/follow/", FollowCreateView.as_view()),
    path("books/followed-books/", FollowedBooksListView.as_view()),
    path("send-email/", EmailNotificationView.as_view()),
]
