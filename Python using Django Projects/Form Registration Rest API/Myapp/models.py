from django.db import models

# Create your models here.


class Forms(models.Model):
	name=models.CharField(max_length=30)
	mobile=models.PositiveIntegerField()
	email=models.EmailField()
	def __str__(safe):
		return safe.name