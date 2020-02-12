from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Login,Login
from .models import Login,Marks
import csv,io
from django import forms
from webapp import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def enter(request):
    if request.method=='POST':

        email=request.POST['email']
        password=request.POST['password']
        try:
            d1=Login.objects.get(email=email)
            if(d1.password==password):
                return render(request,'upload.html')
            else:
                messages.info(request,'*password does not match')
                return render(request,'login.html')
        except Exception:
            messages.info(request,'*invalid email or password')
            return render(request,'login.html')

    else:
        return render(request,'login.html')



def update(request):
    if request.method=='POST':    
        try:
            csv_file=request.FILES['csvfile']
            if csv_file.name.endswith('.csv'):
                data_set=csv_file.read().decode('UTF-8')
                io_string=io.StringIO(data_set)
                for row in csv.reader(io_string, delimiter=",", quotechar="|"):
                    created=Marks(
                        rollnum=row[0],
                        name=row[1],
                        c=row[2],
                        ds=row[3],
                        m3=row[4],
                        architecture=row[5],
                        dsp=row[6])
                    created.save()
            roll_num=request.POST['RollNum']
            name1=request.POST['Name']
            c1=request.POST['c']
            ds1=request.POST['ds']
            m31=request.POST['m3']
            architecture1=request.POST['architecture']
            dsp1=request.POST['dsp']
            try:    
                a=Marks(rollnum=roll_num,name=name1,c=c1,ds=ds1,m3=m31,architecture=architecture1,dsp=dsp1)
                a.save()
                return render(request,'upload.html')
            except:
                return render(request,'upload.html')

        except:
            messages.info(request,'*can not upload empty record')
            return render(request,'upload.html')
    else:
        return render(request,'upload.html')

    
