from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.mail import send_mail
from sms import send_sms

from  StudentApp.models import Student,Purchase,Email
from StudentApp.serializers import StudentSerializer,PurchaseSerializer,EmailSerializer,SmsSerializer



# Create your views here.

@csrf_exempt
def  studentApi(request,id=0):
    if request.method=='GET':
        students=Student.objects.all()
        student_serializer=StudentSerializer(students,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(rollno=student_data['rollno'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update')
    elif request.method=='DELETE':
        student=Student.objects.get(rollno=id)
        student.delete()
        return JsonResponse('Deleted Successfully',safe=False)
@csrf_exempt
def  purchaseApi(request,id=0):
    if request.method=='GET':
        purchases=Purchase.objects.all()
        purchase_serializer=PurchaseSerializer(purchases,many=True)
        return JsonResponse(purchase_serializer.data,safe=False)
    elif request.method=='POST':
        purchase_data=JSONParser().parse(request)
        purchase_serializer=PurchaseSerializer(data=purchase_data)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        purchase_data=JSONParser().parse(request)
        purchase=Purchase.objects.get(vendorid=purchase_data['vendorid'])
        purchase_serializer=PurchaseSerializer(purchase,data=purchase_data)
        if purchase_serializer.is_valid():
            purchase_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to Update')
    elif request.method=='DELETE':
        purchase=Purchase.objects.get(vendorid=id)
        purchase.delete()
        return JsonResponse('Deleted Successfully',safe=False)
@csrf_exempt
def emailApi(request):
    if request.method=="POST":
        email_data=JSONParser().parse(request)
        email_serializer=EmailSerializer(data=email_data)
        email_from = settings.EMAIL_HOST_USER
        rep=email_data['email']
        send_mail(email_data['subject'],email_data['title'],email_from,[rep])
        return JsonResponse('Email send Successfully',safe=False)


@csrf_exempt
def smsApi(request):
    if request.method=="POST":
        sms_data=JSONParser().parse(request)
        sms_serializer=SmsSerializer(data=sms_data)
        sms_from = settings.MOBILE_HOST_NUMBER
        mob=sms_data['mobile']
        send_sms(sms_data['message'],sms_from,[mob],fail_silently=False)
        return JsonResponse('SMS send Successfully',safe=False)

       
        
        