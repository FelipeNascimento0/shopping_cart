from django.urls import path, include
from shirt import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('shirt', views.shirt.ShirtViewSet, basename="shirt")
router.register('purchase', views.purchase.PurchaseViewSet, basename="purchase" )




urlpatterns = [
    path("", include(router.urls))
]