from django.urls import path
from .views import Hello_World, signup, login, get_all_users, get_user_by_email, create_user, update_user, delete_user

urlpatterns = [
    path('hello/', Hello_World, name='hello_world'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('users/', get_all_users, name='get_all_users'),
    path('user/<str:email>/', get_user_by_email, name='get_user_by_email'),
    path('user/create/', create_user, name='create_user'),
    path('user/update/<str:email>/', update_user, name='update_user'),
    path('user/delete/<str:email>/', delete_user, name='delete_user'),
]
