from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.


def signin(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(
                        to="index",
                    )
    elif request.method == "POST" :
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return redirect(
                        to="index",
                    )
                    #return HttpResponse("Authentificated successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
        
    return render(
        request=request,
        template_name="login.html",
        context={
            "page_title": "Login",
            "form": form,
        }
    )


def check_token(request: HttpRequest):
    return HttpResponse("Check Token")


def registration_user(request: HttpRequest):
    return HttpResponse("Registration")


def logout_user(request: HttpRequest):
    return HttpResponse("LogOut")
