from pyexpat import model
from django.db import models

# Create your models here.


class student(models.Model):
    studentid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.TextField()
 
#  def __str__(self):
#         self.'studentid'+ " " + self.'name'
