from django.db import models

# Create your models here.

class Registration(models.Model):
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	mobile=models.PositiveIntegerField()
	email=models.EmailField()
	address=models.TextField()

	def __str__(self):
		return self.fname+" - "+self.lname
