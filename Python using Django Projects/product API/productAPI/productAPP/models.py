from django.db import models

# Create your models here.

class Product(models.Model):
    productid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    quantity=models.PositiveIntegerField()
    type=models.CharField(max_length=50)