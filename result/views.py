from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from login.models import Login,Marks
# Create your views here.

def getmark(request):
    rn=request.POST['rollnum']
    try:
        r=Marks.objects.get(rollnum=rn)
        return render(request,'result.html',{'res':r})
    except:
        messages.info(request,'*invalid Reg Number')
        return redirect("/")