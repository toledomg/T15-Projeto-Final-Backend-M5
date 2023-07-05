from django.urls import path
from .views import BookView, BookDetailView
from copies.views import CopyBookView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("books/<int:pk>/copies/", CopyBookView.as_view()),
]
