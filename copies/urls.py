from django.urls import path
from .views import CopyBookView

urlpatterns =[
    path("books/<int:ok>/copies/", CopyBookView.as_view())
]