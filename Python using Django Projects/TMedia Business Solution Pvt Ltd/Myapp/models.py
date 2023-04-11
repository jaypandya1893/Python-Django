from django.db import models

# Create your models here.


class UserDetail(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)

    def __str__(self):
        return self.name
