from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors={}
        print postData
        if len(postData['name'])<2:
            errors['name']="Name of product must be longer than 2 characters"
        if len(postData['desc'])<2:
            errors['desc']="Description of product must be longer than 3 characters"
        if postData['price']<0 or postData['price']=='':
            errors['price']="Price must be greater than $0"
        return errors
    def create_item(self, postData, id):
        self.create(name=postData['name'], desc=postData['desc'], seller=User.objects.get(id=id), price=postData['price'])

class Item(models.Model):
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    seller=models.ForeignKey(User, related_name="items")
    price=models.FloatField()
    objects=ItemManager()

class Cart(models.Model):
    items = models.ManyToManyField(Item, related_name="carts")
    users = models.ForeignKey(User, related_name="carts")
    qty=models.IntegerField(default=1)



    
