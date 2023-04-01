from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import User, Category, Product, Shop, Seller, ProductImage, Customer, Order


class ProductImageInlineStackedAdmin(admin.StackedInline):
    model = ProductImage
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", 'price', "shop", "shops_seller"]
    inlines = [ProductImageInlineStackedAdmin]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if hasattr(request.user, "seller"):
            queryset = queryset.filter(
                shop__seller=request.user.seller)  # type: ignore

        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "shop":
            if request.user.is_superuser:
                kwargs["queryset"] = Shop.objects.all()
            else:
                kwargs["queryset"] = Shop.objects.filter(
                    seller=request.user.seller)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def shops_seller(self, obj=None):
        return obj.shop.seller  # type: ignore
    shops_seller.short_description = "Sotuvchi"

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser is True:
            return False
        return super().has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser is True:
            return False
        return super().has_change_permission(request, obj)


class CategoryAdmin(MPTTModelAdmin):
    def get_prepopulated_fields(self, request, obj=None) -> dict[str, tuple[str]]:
        return {
            "slug": ("name",)
        }

    # def has_delete_permission(self, request, obj=None) -> bool:
    #     if hasattr(request.user, "seller"):
    #         if obj.shop.seller == request.user.seller:
    #             return True
    #         else:
    #             return False
    #     return super().has_delete_permission(request, obj)


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
