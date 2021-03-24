from rest_framework import permissions
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
          
        if obj.added_by is None:
            return True
          
        return obj.added_by == request.user