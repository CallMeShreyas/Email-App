from django.shortcuts import *
from django.http import *
import time
from app.models import User

def index(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        username=request.POST.get('UserName')
        p1=request.POST.get('p1')
        p2=request.POST.get('p2')
        if(p1==p2):
            user=User(name=name, user_name=username, email=email, password=p1)
            user.save()
            
            return redirect('/email/login')
    else:
        return render(request, 'index.html')
