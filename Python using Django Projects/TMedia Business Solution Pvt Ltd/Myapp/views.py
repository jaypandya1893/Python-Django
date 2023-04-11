from django.shortcuts import render,HttpResponse
from Myapp.models import UserDetail
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def details(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['cpassword']:
            UserDetail.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'],
                confirm_password=request.POST['cpassword'],
            )
            msg="Form Submited Successfuly"
            return render(request,'registration_form.html',{'msg':msg})
        else:
            msg="Password and Confirm Password Does Not Match"
            return render(request,'registration_form.html',{'msg':msg})
    msg=""
    return render(request,"registration_form.html")