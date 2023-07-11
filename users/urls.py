from django.urls import path
from users.views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenRefreshView.as_view()),
]
