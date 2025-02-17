from django.urls import path
from .views import hello_world, signup, login_view

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
]