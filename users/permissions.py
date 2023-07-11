from rest_framework import permissions
from .models import User
from rest_framework.views import View, Request


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsLibraryCollaboratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.method in permissions.SAFE_METHODS and obj == request.user:
            return True

        elif request.user.is_superuser or obj == request.user:
            return True

        return False
