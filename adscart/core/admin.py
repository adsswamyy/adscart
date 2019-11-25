from django.contrib import admin

# Register your models here.
from .models import Item,order_item
# Register your models here.
class item_admin(admin.ModelAdmin):
    list_display=['title','price','discount_price','category','lable','item_sale_type','slug']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Item,item_admin)

admin.site.register(order_item)
# admin.site.register(order)
