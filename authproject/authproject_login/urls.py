from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path(
        route="signin", 
        view=LoginView.as_view(
            template_name="login.html", 
            redirect_authenticated_user=True,
        ),
        name="signin",
    ),
    path(
        route="check_token",
        view=views.check_token,
        name="check_token",
    ),
    path(
        route="signup",
        view=views.registration_user,
        name="signup",
    ),
    path(
        route="logout_user",
        view=views.logout_user,
        name="logout_user",
    )
]

