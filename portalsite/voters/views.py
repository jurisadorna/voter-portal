from django.http import HttpResponse
from django.shortcuts import render,redirect 

# Create your views here.
def home_view(request,*args,**kwargs):
    user=request.user
    return render(request,"base.html",{'user':user})
    
def precinct_view(request,*args,**kwargs):
    return render(request,"precinct.html",{"top5":["8:30 AM - 9:00 AM (30%)","7:30 AM - 8:00 AM(20%)","2:30 PM - 3:00 PM(15%)","8:00 AM - 8:30 AM(10%)","1:00 PM - 1:30 PM(5%)"]})
def redirectview(request,*args,**kwargs):
    r=redirect('Home')
    return r
def createacc_view(request,*args,**kwargs):
    return render(request,"createacc.html",{})
def login_view(request,*args,**kwargs):
    return render(request,"login.html",{})
def scheduling_view(request,*args,**kwargs):
    my_context={"scheds":["8:30 AM - 9:00 AM","7:30 AM - 8:00 AM","2:30 PM - 3:00 PM","8:00 AM - 8:30 AM","1:00 PM - 1:30 PM"],"traffic":[10,23,5,6,12]}
    return render(request,"scheduling.html",my_context)
def pwrecovery_view(request,*args,**kwargs):
    return render(request,"pwrecovery.html",{})
def profile_view(request,*args,**kwargs):
    return render(request,"profile.html",{})
def clang_view(request,*args,**kwargs):
    return render(request,"changelang.html",{})