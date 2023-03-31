from django.db import models

# Create your models here.
class  Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.PositiveIntegerField()
    email=models.EmailField()
    phoneno=models.PositiveIntegerField()
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class  Purchase(models.Model):
    vendorid=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=100)
    orderdate=models.DateField()
    phoneno=models.PositiveIntegerField()
    paymenttype=models.CharField(max_length=100)
    tax=models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Email(models.Model):
    subject=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.email

class Sms(models.Model):
    message=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    def __str__(self):
        return self.mobile