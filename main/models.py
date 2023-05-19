from django.db import models
from django.contrib.auth.models import User,auth
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    disc = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.TextField()
    posted_on = models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.user}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_date = models.DateField(default='2021-02-12')
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)


    def __str__(self):
        return f"{self.user}"



