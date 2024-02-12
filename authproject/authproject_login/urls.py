from django.urls import path
from . import views


urlpatterns = [
    path(
        route="",
        view=views.login_user,
        name="login_user",
    ),
    path(
        route="check_token",
        view=views.check_token,
        name="check_token",
    ),
    path(
        route="registration_user",
        view=views.registration_user,
        name="registration_user",
    ),
    path(
        route="logout_user",
        view=views.logout_user,
        name="logout_user",
    )
]

