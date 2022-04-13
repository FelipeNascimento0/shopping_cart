from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from numpy import round_



class Shirt(models.Model):
        BrandChoices = (
        ("NIKE","nike"),
        ("ADIDAS","adidas"),
        ("OLYMPIKUS","olympikus"),
        ("MIZUNO","mizuno")
        )
        ColorChoices = (
        ("BLACK","black"),
        ("WHITE","white"),
        ("BLUE","blue"),
        ("GREEN","green")
        )

        SizeChoices = (
        ("PP","pp"),
        ("P","p"),
        ("M","m"),
        ("G","g"),
        ("GG","gg")
        )

        shirt_name = models.CharField(max_length=255)
        shirt_brand = models.CharField(max_length=255, choices=BrandChoices, blank=False, null=False)
        shirt_price = models.DecimalField(max_digits=5, decimal_places=2)
        shirt_color = models.CharField(max_length=10, choices=ColorChoices, blank=False, null=False)
        shirt_size = models.CharField(max_length=2, choices=SizeChoices, blank=False, null=False)
        stock = models.IntegerField(default=0)

        def __str__(self):
            return self.shirt_name

class Purchase(models.Model):
    class PurchaseStatus(models.IntegerChoices):
        CAR = 0, "CAR"
        ACCOMPLISHED = 1, "ACCOMPLISHED"
        PAID = 2, "PAID"
        DELIVERED = 3, "DELIVERED"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="purchase")
    status = models.IntegerField(choices=PurchaseStatus.choices, default=PurchaseStatus.CAR)

    def __str__(self):
        return "{}({})".format(self.user, self.status)

    @property
    def total(self):
        queryset = self.items.all().aggregate(total=models.Sum(F('quantity') * F('shirt__shirt_price')))
        return queryset["total"]



class PurchaseItems(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="items")
    shirt = models.ForeignKey(Shirt, on_delete=models.PROTECT, related_name="+")
    quantity = models.IntegerField()
    
        

    



