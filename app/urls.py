from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, SellerViewSet

router = DefaultRouter()

# router.register('user', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('seller', SellerViewSet)

urlpatterns = router.urls


urlpatterns += [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
