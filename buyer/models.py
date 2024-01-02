from django.db import models
from seller.models import Product

# Create your models here.
# one model = one python class = one table in database

class Buyer(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    profile_pic = models.FileField(upload_to = 'buyer_pics', default='sad.jpg')
    address = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 255)

    def __str__(self):
        return self.full_name


class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer.full_name
    
