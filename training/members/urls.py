from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.user_logout, name='logout'),
    path('register_user', views.Register_User, name='register_user')
]
