from django.urls import path
from .views import Hello_World, signup, login

urlpatterns = [
    path('hello/', Hello_World, name='hello_world'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
