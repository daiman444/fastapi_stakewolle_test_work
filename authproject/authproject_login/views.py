from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


def check_token(request: HttpRequest):
    return HttpResponse("Check Token")


def registration_user(request: HttpRequest):
    return HttpResponse("Registration")


def logout_user(request: HttpRequest):
    return HttpResponse("LogOut")
