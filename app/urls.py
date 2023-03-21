from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (CustomerViewSet, SellerViewSet, ShopViewSet,
                    ProductViewSet, ProductImageViewSet,
                    CartViewSet, OrderViewSet, FavouriteViewSet, CategoryViewSet)

router = DefaultRouter()

# router.register('user', UserViewSet)
router.register('customer', CustomerViewSet)
router.register('seller', SellerViewSet)
router.register('shop', ShopViewSet)
router.register('product', ProductViewSet)
router.register('product-image', ProductImageViewSet)
router.register('cart', CartViewSet)
# router.register('cart-item', CartItemViewSet)
router.register('order', OrderViewSet)
# router.register('order-item', OrderItemViewSet)
router.register('favourite', FavouriteViewSet)
router.register('category', CategoryViewSet)

urlpatterns = router.urls


urlpatterns += [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
