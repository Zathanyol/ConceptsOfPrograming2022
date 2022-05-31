from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.createUser, name='createUser'),
    path('inside', views.inside, name='inside'),
    path('logout', views.userLogout, name='logout'),
]