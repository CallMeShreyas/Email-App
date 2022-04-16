from django.shortcuts import render, redirect
from django.http import *
from .models import *
import requests
import json
from datetime import date
# Create your views here.
username = []
pwd = []
u_name = []


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
            # username = uname
            # pwd = password
            username.append(uname)
            pwd.append(password)
            u_name.append(user.name)
            responce = requests.get('https://shreyas001.pythonanywhere.com/api/emaildb/')
            resp = responce.json()
            mails = []
            for i in resp:
                if i['receiver'] == uname:
                    mails.append(i)
            return render(request, "home.html", {'uname': uname, 'emails': mails, 'user': user})
        else:
            return HttpResponse("<h1> Logged Out </h1>")
        # return render(request, 'sentmail.html')
        
def compose_success(request):

        receiver=request.POST.get('rec')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        today=date.today()
        responce=requests.post('https://shreyas001.pythonanywhere.com/api/emaildb/', data={'sender': username[0], 'receiver': receiver , 'subject': subject , 'message': message , 'date':today})

        if responce.status_code == 201:
            user = User.objects.get(user_name=username[0])
            if user.password == pwd[0]:
                responce = requests.get('https://shreyas001.pythonanywhere.com/api/emaildb/')
                resp = responce.json()
                mails = []
                for i in resp:
                    if i['receiver'] == username[0]:
                        mails.append(i)
                return render(request, "home.html", {'uname': username[0], 'emails': mails, 'user': username[0]})
            else:
               return HttpResponse("<h1> Invalid Credentials </h1>")

def sentmails(request):
    user = User.objects.get(user_name=username[0])
    if user.password == pwd[0]:
        responce = requests.get('https://shreyas001.pythonanywhere.com/api/emaildb/')
        resp = responce.json()
        mails = []
        for i in resp:
            if i['sender'] == username[0]:
                mails.append(i)
        return render(request, "sentmail.html", {'uname': username[0], 'emails': mails, 'user': username[0]})

def success(request):
    user = User.objects.get(user_name=username[0])
    if user.password == pwd[0]:
        responce = requests.get('https://shreyas001.pythonanywhere.com/api/emaildb/')
        resp = responce.json()
        mails = []
        for i in resp:
            if i['receiver'] == username[0]:
                mails.append(i)
        return render(request, "home.html", {'uname': username[0], 'emails': mails, 'user': user})

def compose(request):
    user = User.objects.get(user_name=username[0])
    if user.password == pwd[0]:
        return render(request, 'compose.html')

def logout(request):
    username.remove(username[0])
    pwd.remove(pwd[0])
    u_name.remove(u_name[0])
    return render(request, 'index.html')