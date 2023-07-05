from django.urls import path
from .views import CopyBookView

urlpatterns = [
    path("copies/<int:pk>/books/", CopyBookView.as_view())
]