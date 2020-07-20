from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100) # max = req
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=300)
    summary     = models.TextField()
    active      = models.BooleanField(default=True)
    male        = models.BooleanField(null=True)
    female      = models.BooleanField(default=True, null=True)