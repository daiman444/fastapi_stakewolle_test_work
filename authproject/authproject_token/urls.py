from django.urls import path
from . import views


urlpatterns = [
    path(
        route="",
        view=views.IndexView.as_view(),
        name="index",
    ),
    # path(
    #     route="show_token",
    #     view=views.show_token,
    #     name="show_token",
    # ),
    path(
        route="create_token",
        view=views.create_token,
        name="create_token",
    ),
    path(
        route="delete_token",
        view=views.delete_token,
        name="delete_token",
    ),
    
]

