from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about', views.about, name="about"),
    path('login', views.login, name='login'),
    path('', views.register, name="register"),
]