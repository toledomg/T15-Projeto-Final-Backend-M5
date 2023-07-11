from django.urls import path
from users.views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

from users.views import login_view, index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenRefreshView.as_view()),
    # Reset Password
    # path("users/login/", login_view, name="login"),
    path("users/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "users/password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password/password-reset.html"
        ),
        name="password_reset",
    ),
    path(
        "users/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password/password-reset-done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "users/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password/password-reset-confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "users/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password/password-reset-complete.html"
        ),
        name="password_reset_complete",
    ),
]
