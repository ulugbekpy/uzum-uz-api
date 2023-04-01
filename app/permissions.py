from rest_framework.permissions import BasePermission


class OrderPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated is True:
            return True

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'customer'):
            if request.user == obj.customer:
                return True


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.is_authenticated is True:
            return True
        else:
            return False

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'user'):
            if request.user == obj.user:
                return True
            else:
                return False

        return super().has_object_permission(request, view, obj)
