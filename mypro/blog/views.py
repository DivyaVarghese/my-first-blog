from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Register,Postadd,Postedit
import datetime
# Create your views here.
def about1(request):
	return render(request,'about.html',{})
	
def home(request):
	return render(request,'index.html',{})

def gallery(request):
	return render(request,'gallery.html',{})

def contact(request):
	return render(request,'contact.html',{})


def reg(request):
	if request.method=='POST':
		uname=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		country=request.POST.get('country')
		u=User.objects.filter(email=email).exists()
		if not u:
			r=User.objects.create_user(username=email,first_name=uname,email=email,password=password)
			ureg=Register(user1=r,country=country)
			ureg.save()
			return render(request,'login.html',{})
		else:
			error="Already existing"
			return render(request,'register.html',{'error':error})		
	else:
		return render(request,'register.html',{})


def login1(request):
	if request.method=='POST':
		uname=request.POST.get('uname')
		password=request.POST.get('password')
		u=authenticate(request,username = uname, password = password)
		
		if u:
			login(request,u)
			return render(request,'blogadd.html',{'uname':uname})
		else:
			error="NOT A VALID ENTRY"
			return render(request,'login.html',{'error':error})
	else:
		return render(request,'login.html',{})

def signout(request):

	logout(request)
	return render(request,'index.html',{})


def blogadd(request):
	uu=User.objects.get(username=request.user)

	if request.method=='POST':
		title=request.POST.get('title')
		text=request.POST.get('text')
		img=request.POST.get('pic')
		r=User.objects.get(username=request.user)
		r2=Register.objects.get(user1=r)
		uadd=Postadd(user1=r2,title=title,text=text,photo=img)
		uadd.save()
		p=Postadd.objects.all()
		return render(request,'bloglist.html',{'user':p})
	else:
		return render(request,'blogadd.html',{'uname':uu})

def blogs(request):
	if request.method=='POST':	
		u1=User.objects.get(username=request.user)
		u2=u1.first_name
		u3=Register.objects.get(user1=u1)
		u4=Postadd.objects.get(user1=u3)
		# u5=u4.title
		# print(u5)
		return render(request,'blogedit.html',{'user':u2,'u':u4})
	else:
		return render(request,'bloglist.html',{})


def blogedit(request):
	u=User.objects.get(username=request.user)
	if request.method=='POST':
		title=request.POST.get('title')
		text=request.POST.get('text')
		u=User.objects.get(username=request.user)
		u1=Register.objects.get(user1=u)
		Postadd.objects.filter(user1=u1).delete()
		p=Postadd(user1=u1,title=title,text=text)
		p.save()
		p1=Postadd.objects.all()
		
		
		return render(request,'bloglist.html',{'user':p1})
	else:
		return render(request,'blogedit.html',{'user':u})


		

