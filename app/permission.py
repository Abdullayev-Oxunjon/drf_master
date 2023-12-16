from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user.is_authenticated and request.user.is_staff):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or (request.user.is_authenticated and request.user.is_staff):
            return True
        return False

    # nima