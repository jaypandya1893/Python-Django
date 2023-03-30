from django.shortcuts import render,redirect
from .models import Contact,User

# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			mobile=request.POST['mobile'],
			email=request.POST['email'],
			remark=request.POST['remark'],
			)
		msg="Contact Save Successfully"
		contacts=Contact.objects.all().order_by("-id")[:2]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by("-id")[:2]
		return render(request,'contact.html',{'contacts':contacts})
		
def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Regiostered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
				fname=request.POST['fname'],
				lname=request.POST['lname'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				address=request.POST['address'],
				gender=request.POST['gender'],
				password=request.POST['password'],
				)
				msg="User Sign Up Successfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Match" 
				return render(request,'signup.html',{'msg':msg})
	else:		
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['opassword']:
			if request.POST['npassword']==request.POST['cpassword']:
				user.password=request.POST['npassword']
				user.save()
				msg="Password Changed Successfully"
				return redirect('logout')
			else:
				msg="Password & Confirm Password Does Not Match" 
				return render(request,'changepassword.html',{'msg':msg})
		else:
			msg="Old Password Does Not Match" 
			return render(request,'changepassword.html',{'msg':msg})
	else:
		return render(request,'changepassword.html')