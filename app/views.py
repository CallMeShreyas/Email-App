from django.shortcuts import render
from django.http import *
from .models import *
import requests
import json
# Create your views here.
username = ''
pwd = ''


def login(request):
    # return HttpResponse("<h1>Working</h1>")
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
    # return HttpResponse("<h1>Working</h1>")


def home(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        password = request.POST.get('p1')
        user = User.objects.get(user_name=uname)
        if user.password == password:
            username = uname
            pwd = password
            # username.append(uname)
            # pwd.append(password)
            responce = requests.get('https://shreyas001.pythonanywhere.com/api/emaildb/')
            resp = responce.json()
            mails=[]
            for i in resp:
                if i['receiver'] == uname:
                    mails.append(i)
            return render(request, "home.html", {'uname': username, 'emails': mails, 'user':user})
    else:
        return render(request, 'sentmail.html')

def sentmails(request): 
    if username is not null:
        user=User.objects.get(user_name=username[0])
        return render(request, 'sentmail.html')


def compose(request):
    return render(request, 'compose.html')