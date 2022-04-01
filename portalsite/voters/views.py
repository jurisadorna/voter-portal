from random import randint
from re import L
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate, login,logout
from .models import Precinct, User,Voter,Admin,Repre
from django.contrib import messages
# Create your views here.
def home_view(request,*args,**kwargs):
    user=request.user
    full_name=''
    if user.is_authenticated:
        full_name=user.first_name+" "+user.last_name
    return render(request,"base.html",{'user':user, 'name':full_name})

def profile_view(request,*args,**kwargs):
    user=request.user
    full_name=''
    if not user.is_authenticated:
        return redirect('Home')
    if user.is_voter:
        name=Voter.objects.get(user=user)
        full_name=name.user.first_name+" "+name.user.last_name
        precinct=Precinct.objects.get(pNum=name.pNum)
        print(precinct)
        return render(request,"profile.html",{'user':user,'name':full_name, 'info':name,'pr':precinct})
    voters=Repre.objects.filter(user=user)
    print(user.username)
    rep=User.objects.values('first_name','last_name').get(username=user.username)
    full_name=rep['first_name']+" "+rep['last_name']
    pr=[]
    for vtr in voters:
        precinct=Precinct.objects.get(pNum=vtr.pNum)
        pr.append(precinct)
    info=zip(voters,pr)
    return render(request,"profile.html",{'user':user,'name':full_name, 'info':info})

def precinct_view(request,*args,**kwargs):
    a=randint(1,20)
    b=randint(0,30)
    user=request.user
    full_name=''
    if not user.is_authenticated:
        return redirect('Home')
    name=Voter.objects.get(user=user)
    full_name=name.user.first_name+" "+name.user.last_name
    return render(request,"precinct.html",{'name':full_name,"top5":["8:30 AM - 9:00 AM (30%)","7:30 AM - 8:00 AM(20%)","2:30 PM - 3:00 PM(15%)","8:00 AM - 8:30 AM(10%)","1:00 PM - 1:30 PM(5%)"],'v':a,'nv':b})
def redirectview(request,*args,**kwargs):
    r=redirect('Home')
    return r
def createacc_view(request,*args,**kwargs):
    return render(request,"createaccount.html",{})

def scheduling_view(request,*args,**kwargs):
    my_context={"scheds":["8:30 AM - 9:00 AM","7:30 AM - 8:00 AM","2:30 PM - 3:00 PM","8:00 AM - 8:30 AM","1:00 PM - 1:30 PM"],"traffic":[10,23,5,6,12]}
    return render(request,"scheduling.html",my_context)
def pwrecovery_view(request,*args,**kwargs):
    return render(request,"pwrecovery.html",{})

def clang_view(request,*args,**kwargs):
    return render(request,"changelang.html",{})

def login_view(request,*args,**kwargs):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            user=User.objects.get(username=username)
            if user is not None and password==user.password:
                print("ok")
                login(request,user)
                return redirect("Home")
            else:
                messages.success(request,"Invalid Credentials")
                return redirect("login")
        except User.DoesNotExist:
                messages.success(request,"Invalid Credentials")
                return redirect("login")
    else:
        return render(request,"login.html",{})
def logout_acc(request):
    logout(request)
    return redirect("Home")

def testview(request): #for testing of incorporated css and js files
    return render(request,"charts.html",{})