from itertools import product
from django.db import models

# Create your models here.
class Product(models.Model): # type: ignore
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField()
    features = models.BooleanField()