from django.urls import path

from . import views

urlpatterns = [
    path("", views.Homepage, name="homepage"),
    path("login", views.Login, name="login"),
    path("password/new", views.Forgetpassword, name="forgetpassword"),
    path("store", views.Forgetpassword, name="store"),


]