from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup, name='signup'),
    path('signup', views.signup, name='signup'),
    path('home',views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('error_403', views.error_403, name='error_403'),
]