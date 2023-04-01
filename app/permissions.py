from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            if hasattr(request.user, 'customer'):
                return True
            else:
                return False

        if request.method == 'DELETE':
            if request.user.is_superuser or request.user == obj.customer:
                return True
            else:
                return False

        if request.method == 'PUT':
            if request.user == obj.customer:
                return True
            else:
                return False

        if request.method == 'PATCH':
            if request.user == obj.customer:
                return True
            else:
                return False

        return super().has_object_permission(request, view, obj)


class SellerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT':
            if request.user == obj.user:
                return True
            else:
                return False

        if request.method == 'PATCH':
            if request.user == obj.user:
                return True
            else:
                return False

        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            else:
                return False

        if request.method == 'POST':
            return True

        return super().has_object_permission(request, view, obj)
