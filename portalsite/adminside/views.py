from django.shortcuts import render,redirect
# Create your views here.
def ahome_view(request,*args,**kwargs):
    return render(request,"ahome.html",{})
def count_view(request,*args,**kwargs):
    return render(request,"ballotcount.html",{})
def redir_view(request,*args,**kwargs):
    r=redirect('login')
    return r