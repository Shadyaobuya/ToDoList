from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
now=datetime.now

def hellow(request):
    # return HttpResponse("Hello World")
    return render(request,"one/index.html",{
        "date":now
    })

def jayne(request):
    return HttpResponse("Hello jayne")
def greeting(request,name):
    return render(request,"one/index.html",{
        "name":name.capitalize(),
        "date":now
    })

    return HttpResponse("Hello {}".format(name.capitalize()))
