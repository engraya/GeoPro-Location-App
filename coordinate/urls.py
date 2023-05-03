from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('geo_api', views.geo_api, name="geo_api"),
    path("register", views.registerUser, name="registerUser"),
    path("login", views.loginUser, name="loginUser"),
    path("logout", views.logoutUser, name="logoutUser"),
    path("profile", views.profile, name="profile"),
    path("", views.landingPage, name="landingPage"),
    path("infoPage/", views.infoPage, name="infoPage"),
]
