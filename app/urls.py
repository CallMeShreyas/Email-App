from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login', views.loggin),
    path('signup', views.signup),
    path('home', views.home),
    path('sent', views.sentmails),
    path('compose', views.compose),
    path('email_sent', views.compose_success),
    path('success', views.success),
    path('logged_out', views.loggout),
    path('view/<int:id>', views.viewmsg)
]