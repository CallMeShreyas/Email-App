from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import json
from datetime import date


# username = []
# pwd = []
# u_name = []

def loggin(request):
    # return HttpResponse("<h1>Working</h1>")
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")
    # return HttpResponse("<h1>Working</h1>")


def home(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('p1')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            responce = requests.get(
                'https://shreyas001.herokuapp.com/api/emaildb/')
            resp = responce.json()
            mails = []
            for i in resp:
                if i['receiver'] == username:
                    mails.append(i)
            return render(request, "home.html", {'uname': username, 'emails': mails, 'user': user})


def compose_success(request):
    current_user = request.user
    receiver = request.POST.get('rec')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    today = date.today()
    responce = requests.post('https://shreyas001.herokuapp.com/api/emaildb/', data={
                             'sender': current_user.username, 'receiver': receiver, 'subject': subject, 'message': message, 'date': today})

    if responce.status_code == 201:
        responce = requests.get(
            'https://shreyas001.herokuapp.com/api/emaildb/')
        resp = responce.json()
        mails = []
        for i in resp:
            if i['receiver'] == current_user.username:
                mails.append(i)
        return render(request, "home.html", {'uname': current_user.username, 'emails': mails, 'user': current_user})


def sentmails(request):
    # user = User.objects.get(user_name=username[0])
    current_user = request.user
    responce = requests.get(
        'https://shreyas001.herokuapp.com/api/emaildb/')
    resp = responce.json()
    mails = []
    for i in resp:
        if i['sender'] == current_user.username:
            mails.append(i)
    return render(request, "sentmail.html", {'uname': current_user.username, 'emails': mails})


def success(request):
    current_user = request.user
    responce = requests.get(
        'https://shreyas001.herokuapp.com/api/emaildb/')
    resp = responce.json()
    mails = []
    for i in resp:
        if i['receiver'] == current_user.username:
            mails.append(i)
    return render(request, "home.html", {'uname': current_user.username, 'emails': mails, 'user': current_user})


def compose(request):
    return render(request, 'compose.html')


def loggout(request):
    logout(request)
    return render(request, 'index.html')


def viewmsg(request, id):
    current_user=request.user
   
    responce = requests.get(
            'https://shreyas001.herokuapp.com/api/emaildb/')
    resp = responce.json()
    for i in resp:
            if i['id'] == id:
                return render(request, 'viewmsg.html', {'email': i})
