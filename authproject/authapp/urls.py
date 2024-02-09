from django.urls import path
from . import views

urlpatterns = [
    path(
      route='',
      view=view  
    ),
    path(
        route='login/',
        view=views.user_login,
        name='login',
    )
]