from django.db import models
from products.models import Products
from users.models import User

class Cart_model(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40,null=True,blank=True,db_index=True)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart_model,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,null=True,blank=True,on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField(default=1)
