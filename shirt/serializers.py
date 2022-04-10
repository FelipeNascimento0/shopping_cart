from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from shirt.models import Shirt, Purchase, PurchaseItems
from numpy import source



class ShirtSerializer(ModelSerializer):
    class Meta:
        model = Shirt
        fields = '__all__'

class PurchaseItemsSerializer(ModelSerializer):

    total = SerializerMethodField()
    shirt_name = CharField(source="shirt.shirt_name")
    shirt_price = CharField(source="shirt.shirt_price")



    class Meta:
        model = PurchaseItems
        fields = ('shirt_name','shirt_price','quantity','total')
        depth = 2

    def get_total(self, instance):
        result = instance.quantity * instance.shirt.shirt_price
        return round(result, 2)


class PurchaseSerializer(ModelSerializer):
    user = CharField(source="user.username")
    items = PurchaseItemsSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ('id','user','items','total')


class CreateUpdateItemsSerializer(ModelSerializer):
    class Meta:
        model = PurchaseItems
        fields = ('shirt','quantity')

class CreateUpdatePurchaseSerializer(ModelSerializer):
    items = CreateUpdateItemsSerializer(many=True)
    class Meta:
        model = Purchase
        fields = ('user','items')

    def create(self, validated_data):
        items = validated_data.pop("items")
        purchase = Purchase.objects.create(**validated_data)
        for item in items:
            PurchaseItems.objects.create(purchase=purchase, **item)
        purchase.save()
        return purchase

    def update(self, instance, validated_data):
        items = validated_data.pop("items")
        if items:
            instance.items.all().delete()
            for item in items:
                PurchaseItems.objects.create(purchase= instance, **item)
            instance.save()
        return instance




