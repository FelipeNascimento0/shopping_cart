from django.contrib import admin
from .models import  Shirt, Purchase, PurchaseItems 


class ShirtAdmin(admin.ModelAdmin):
    list_display = ("shirt_name","shirt_brand","shirt_price","shirt_color","shirt_size","stock",)

admin.site.register(Shirt, ShirtAdmin)




class PurchaseItemsInline(admin.TabularInline):
    model = PurchaseItems

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseItemsInline,) 





