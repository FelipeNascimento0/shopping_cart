from django.urls import path, include
from shirt import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('shirt', views.shirt.ShirtViewSet, basename="shirt")
router.register('purchase', views.purchase.PurchaseViewSet, basename="purchase" )




urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls))
]