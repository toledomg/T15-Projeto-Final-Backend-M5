from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm  # PasswordResetForm

from .models import User
from .serializers import UserSerializer
from .permissions import IsLibraryCollaboratorOrOwner, IsAdminOrReadOnly


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = User.objects.filter(email=email).first()

            if user:
                user = authenticate(username=user.username, password=password)

            if user:
                login(request, user)
                return redirect("/")
            else:
                msg = "Usuário ou senha inválidos"
        else:
            msg = "Erro ao logar"

    return render(request, "users/sign-in.html", {"form": form, "msg": msg})


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html", {"msg": "Home Page Biblioteka!"})


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
