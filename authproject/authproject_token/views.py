from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from .models import Token

# Create your views here.


class IndexView(generic.ListView):
    model = Token
    template_name = "index.html"
    context_object_name = "tokens"
    
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.user.is_authenticated:
            token = Token.objects.filter(active=True)
            return token
            
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = {
            "signin": "Sign In/",
            "signup": "Sign Up"
            
        }
        return context


def show_token(request: HttpRequest):
    return HttpResponse("Your Tokens")


def create_token(request: HttpRequest):
    return HttpResponse("Create Token")


def delete_token(request: HttpRequest):
    return HttpResponse("Delete Token")
    