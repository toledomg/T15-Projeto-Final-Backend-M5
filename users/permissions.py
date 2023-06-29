from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsLibraryCollaboratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.library_collaborator or request.user.is_authenticated and obj == request.user)
