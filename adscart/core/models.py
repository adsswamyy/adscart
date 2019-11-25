from django.db import models

# Create your models here.
#from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
CATAGORY_CHOICES=(
('Shirt','Shirt'),
('Sport wear','Sport wear'),
('Outwear','Outwear')
)
LABLE_CHOICES=(
('Primary','primary'),
('Secondary','secondary'),
('Danger','danger')
)
Item_Sale_Choices=(
('NEW','NEW'),
('Bestseller','Bestseller')
)
class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField(blank=True)
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATAGORY_CHOICES,max_length=20)
    lable=models.CharField(choices=LABLE_CHOICES,max_length=20)
    item_sale_type=models.CharField(choices=Item_Sale_Choices,max_length=11)
    slug=models.SlugField(max_length=200)
    Description=models.TextField(default='')
    def get_absolute_url(self):
        return reverse('details',kwargs={
        'pk':self.pk
        })
    def __str__(self):
        return self.title

class order_item(models.Model):
    items=models.ForeignKey(Item,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.title

class order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(order_item)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
