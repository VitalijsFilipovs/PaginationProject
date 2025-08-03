from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Только владелец объекта может изменять его. Остальные — только чтение.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запретить изменение, если не автор
        return obj.owner == request.user
