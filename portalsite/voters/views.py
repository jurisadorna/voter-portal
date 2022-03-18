from re import L
from django.http import HttpResponse
from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login,logout
from .models import User,Voter,Admin
# Create your views here.
def home_view(request,*args,**kwargs):
    user=request.user
    full_name=''
    if user.is_authenticated:
        name=Voter.objects.get(user=user)
        full_name=name.user.first_name+" "+name.user.last_name
    return render(request,"base.html",{'user':user, 'name':full_name})
    
def precinct_view(request,*args,**kwargs):
    return render(request,"precinct.html",{"top5":["8:30 AM - 9:00 AM (30%)","7:30 AM - 8:00 AM(20%)","2:30 PM - 3:00 PM(15%)","8:00 AM - 8:30 AM(10%)","1:00 PM - 1:30 PM(5%)"]})
def redirectview(request,*args,**kwargs):
    r=redirect('Home')
    return r
def createacc_view(request,*args,**kwargs):
    return render(request,"createacc.html",{})

def scheduling_view(request,*args,**kwargs):
    my_context={"scheds":["8:30 AM - 9:00 AM","7:30 AM - 8:00 AM","2:30 PM - 3:00 PM","8:00 AM - 8:30 AM","1:00 PM - 1:30 PM"],"traffic":[10,23,5,6,12]}
    return render(request,"scheduling.html",my_context)
def pwrecovery_view(request,*args,**kwargs):
    return render(request,"pwrecovery.html",{})
def profile_view(request,*args,**kwargs):
    return render(request,"profile.html",{})
def clang_view(request,*args,**kwargs):
    return render(request,"changelang.html",{})

def login_view(request,*args,**kwargs):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=User.objects.get(username=username)
        if user is not None and password==user.password:
            print("ok")
            login(request,user)
            cred=Voter.objects.get(user=user)
            return redirect("Home",)
    else:
        return render(request,"login.html",{})
def logout_acc(request):
    logout(request)
    return redirect("Home")