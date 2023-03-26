from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class ProductPermission(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return [AllowAny]
        else:
            pass

    def has_object_permission(self, request, view, obj):
        return obj.shop.seller.user == request.user
