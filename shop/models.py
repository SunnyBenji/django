from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name
# Create your models here.
