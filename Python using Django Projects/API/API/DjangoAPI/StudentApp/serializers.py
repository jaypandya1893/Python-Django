from rest_framework import serializers
from StudentApp.models import Student,Purchase,Email,Sms

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('name','rollno','email','phoneno','department')
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:    
        model=Purchase
        fields=('vendorid','name','orderdate','phoneno','paymenttype','tax')

class EmailSerializer(serializers.ModelSerializer):
    class Meta:    
        model=Email
        fields=('email','subject','title')
class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sms
        fields=('message','mobile')