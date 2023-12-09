from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)

class Affiliate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
   



