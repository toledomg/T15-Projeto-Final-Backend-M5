from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsLibraryCollaboratorOrOwner


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return serializer.save()

    @extend_schema(
        operation_id="users_list",
        description="Rota para Listar Users",
        summary="Listar Users",
        exclude=False,
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLibraryCollaboratorOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    @extend_schema(exclude=True)
    def put(self, request, *args, **Kwargs):
        return super().put(request, *args, **Kwargs)