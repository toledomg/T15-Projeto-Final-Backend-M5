from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

from .models import User
from .serializers import UserSerializer
from .permissions import IsLibraryCollaboratorOrOwner


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
