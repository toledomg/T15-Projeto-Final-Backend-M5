from django.urls import path
from .views import LoanView, LoanDetailView, UserLoansDetailView

urlpatterns = [
    path("loans/", LoanView.as_view()),
    path("loans/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
    path("loans/user/", UserLoansDetailView.as_view()),
]
