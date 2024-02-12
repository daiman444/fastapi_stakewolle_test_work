from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request: HttpRequest):
    if request.user.is_authenticated:
        return HttpResponse("Hello, World")
    else:
        return HttpResponse("Login/Registration")


def show_token(request: HttpRequest):
    return HttpResponse("Your Tokens")


def create_token(request: HttpRequest):
    return HttpResponse("Create Token")


def delete_token(request: HttpRequest):
    return HttpResponse("Delete Token")
    