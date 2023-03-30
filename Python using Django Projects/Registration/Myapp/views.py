from django.shortcuts import render,HttpResponse

# Create your views here.

from Myapp.models import Registration

def Registrations(request):
	if request.method=="POST":
		Registration.objects.create(
			fname=request.POST['fname'],
			lname=request.POST['lname'],
			gender=request.POST['gender'],
			mobile=request.POST['mobile'],
			email=request.POST['email'],
			address=request.POST['address'],
			)
	return render(request,"form.html")



