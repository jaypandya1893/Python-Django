from rest_framework import serializers
from Myapp.models import student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('studentid','name','department','mobile','email','address')