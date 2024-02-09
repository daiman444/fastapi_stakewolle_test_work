from django.urls import path
from . import views

urlpatterns = [
    path(
      route='',
      view=views.index,
      name='index',  
    ),
    path(
        route='login/',
        view=views.user_login,
        name='login',
    )
]