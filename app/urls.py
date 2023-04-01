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
                    CartViewSet, OrderViewSet, FavouriteViewSet, CategoryViewSet,
                    RegisterView)

router = DefaultRouter()

router.register('customer', CustomerViewSet)
router.register('seller', SellerViewSet)
router.register('shop', ShopViewSet)
router.register('product', ProductViewSet)
router.register('product-image', ProductImageViewSet)
router.register('cart', CartViewSet)
router.register('order', OrderViewSet)
router.register('favourite', FavouriteViewSet)
router.register('category', CategoryViewSet)

urlpatterns = router.urls


urlpatterns += [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
