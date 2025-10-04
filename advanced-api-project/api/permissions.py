from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only requests for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admins can modify
        return request.user and request.user.is_staff
