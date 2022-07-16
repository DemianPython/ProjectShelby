from django.contrib import admin
from django.urls import path, include
from .views import logout_view, register_view, login_view, user_registration

urlpatterns = [
    path("user-registration/", user_registration , name="user_registration"),
    path("register/", register_view  , name="register"),
    path("login/", login_view , name="login"),
    path("logout/", logout_view  , name="logout"),
]