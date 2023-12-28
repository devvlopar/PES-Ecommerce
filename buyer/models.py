from django.db import models

# Create your models here.
# one model = one python class = one table in database

class Buyer(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    profile_pic = models.FileField(upload_to = 'buyer_pics', default='sad.jpg')
    address = models.CharField(max_length = 255)
    mobile = models.CharField(max_length = 255)

    # def __str__(self):
    #     return self.email
