from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Myapp.models import student
from Myapp.serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
# Create your views here.


@csrf_exempt
def Student(request,id=0):
    if request.method=="POST":
        student_json=JSONParser().parse(request)
        student_serializer=StudentSerializers(data=student_json)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Add Successfully",safe=False)
        return JsonResponse("Error in Fill Details",safe=False)
    
    elif request.method=="PUT":
        student_json=JSONParser().parse(request)
        student_data=Student.objects.get(studentid=id)
        student_serializer=StudentSerializers(student_data,data= student_json)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Edit Successfully",safe=False)
        return JsonResponse("Error To Edit Details",safe=False)
    
    elif request.method=="GET":
        student_data=Student.objects.fillter(studentid=id)
        student_serializer=StudentSerializers(student_data,mbany=True)
        return JsonResponse(student_serializer.data,safe=False)
            
    elif request.method=="DELETE":
        student_data=Student.objects.get(studentid=id)
        student_data.delete()
        return JsonResponse("Deleted Successfully",safe=False)
        


