#Importing modules for backend
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "indexpage"),
    path('signIn/',views.signIn, name= "signIn"),
    path('home/',views.home,name= "homepage"),
    path('signUp/',views.signUp,name = 'signUpPage')
]

