def RoleRequired(roles):
    from rest_framework.permissions import BasePermission

    class _RolePermission(BasePermission):
        def has_permission(self, request, view):
            return (
                request.user and
                request.user.is_authenticated and
                request.user.role in (
                    roles if isinstance(roles, list) else [roles])
            )

    return _RolePermission
