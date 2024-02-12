from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
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
            active_tokens = Token.objects.filter(active=True)
            for token in active_tokens:
                if not token.token_is_alive():
                    token.active = False
                    token.save()
            if not token.token_is_alive():
                return token
            else:
                return None
            
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["token"] = self.get_queryset()
            context['links'] = {
                "create_token": "CreateToken",                
            }
        else:
            context['links'] = {
                "signin": "SignIn",
                "signup": "SignUp"
            }
        return context


# class ShowTokenView(generic.ListView):
#     return HttpResponse("Your Tokens")


def create_token(request: HttpRequest):
    return HttpResponse("Create Token")


def delete_token(request: HttpRequest):
    return HttpResponse("Delete Token")
    