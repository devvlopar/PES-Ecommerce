from django.db import models

# Create your models here.

class SellerTable(models.Model):
    gst_number = models.CharField(max_length= 255)
    seller_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to='seller_profiles', default='sad.jpg')

    def __str__(self):
        return self.seller_name