from django.shortcuts import render,HttpResponse
from Myapp.models import Forms

# Create your views here.


def forms(request):
	if request.method=="POST":
		Forms.objects.create(
			name=request.POST['name'],
			mobile=request.POST['mobile'],
			email=request.POST['email'],
			)
	return render(request,"form.html")

