from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def login_user(request: HttpRequest):
    return HttpResponse("login")


def check_token(request: HttpRequest):
    return HttpResponse("Check Token")


def registration_user(request: HttpRequest):
    return HttpResponse("Registration")


def logout_user(request: HttpRequest):
    return HttpResponse("LogOut")
