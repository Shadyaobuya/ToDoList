from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms


# Create your views here.

# class Login(forms.Form):
#     username=forms.CharField(label="Username")
#     password=forms.PasswordInput(label="Password")

def login(request):
    return render(request,"login/index.html")

def signup(request):
    return HttpResponse(request,"Hey You")