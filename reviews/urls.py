from django.urls import path
from .views import ReviewView, ReviewDetailView

urlpatterns = [
    path("reviews/", ReviewView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailView.as_view()),
]
