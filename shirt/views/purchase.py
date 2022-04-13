from unicodedata import name
from shirt.models import Purchase
from shirt.serializers import PurchaseSerializer, CreateUpdatePurchaseSerializer
from rest_framework.viewsets import ModelViewSet

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    #serializer_class = PurchaseSerializer
    def get_serializer_class(self):
        if self.action =="list" or self.action =="retrieve":
            return PurchaseSerializer
        return CreateUpdatePurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="administrator"):
            return Purchase.objects.all()
        return Purchase.objects.filter(user=user) 
