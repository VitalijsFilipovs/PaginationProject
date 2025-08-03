from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение, позволяющее редактировать объект только владельцу.
    """

    def has_object_permission(self, request, view, obj):
        # Безопасные методы (GET, HEAD, OPTIONS) разрешены всем авторизованным
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверка, является ли пользователь владельцем объекта
        return obj.owner == request.user
