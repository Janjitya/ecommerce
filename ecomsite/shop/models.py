from django.db import models

# Create your models here.

class Products(models.Model):

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to="product_images/", default="product_images/no_image.jpg")


    def __str__(self):
        return self.title
    
class Order(models.Model):

    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    total = models.CharField(max_length=100, default=0)
