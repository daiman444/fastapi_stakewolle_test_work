from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def show_token(request: HttpRequest):
    page_title = "Token"
    return render(
        request=request,
        template_name="index.html",
        context={
            "page_title": page_title,
        }
    )