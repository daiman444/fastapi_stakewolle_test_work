from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def index(request: HttpRequest):
    return render(
        request=request,
        template_name="index.html",
    )


def user_login(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return HttpResponse("Authentificated successfully")
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
            "title": "Login",
            "form": form,
        }
    )
