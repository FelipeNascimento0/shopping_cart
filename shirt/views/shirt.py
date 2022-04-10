from shirt.models import Shirt
from shirt.serializers import ShirtSerializer
from rest_framework.viewsets import ModelViewSet


class ShirtViewSet(ModelViewSet):
    queryset = Shirt.objects.all()
    serializer_class = ShirtSerializer