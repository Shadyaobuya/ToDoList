from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

 
# Create your views here.
list_of_tasks=[]

class NewTask(forms.Form):
    task=forms.CharField(label="Task",widget=forms.TextInput(attrs={"class":"form-control",'style': 'width: 300px;'}))
    priority=forms.IntegerField(label="Priority",max_value=10,min_value=1,widget=forms.NumberInput(attrs={"class":"form-control ",'style': 'width: 300px;'}))
    duration=forms.IntegerField(label="Duration in Minutes",min_value=30,widget=forms.NumberInput(attrs={"class":" form-control","min":"30",'style': 'width: 300px;'}))

# class Login(forms.Form):
#      username=forms.CharField()
#      password=forms.PasswordInput( )

# def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('login'))
#     return render(request,"tasks/login.html")


def login_page(request):
    if request.method=="POST":
        usern=request.POST["username"]
        passw=request.POST["password"]
        user=authenticate(request,username=usern,password=passw)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'tasks/login.html',{
                "message":"Invalid Username or Password"
            })
    return render(request,"tasks/login.html")
    

    

def my_tasks(request):
    return render(request,'tasks/index.html',{
        "all_tasks":list_of_tasks
    })

def addTask(request):
    if request.method=="POST":
        form_data=NewTask(request.POST)
        if form_data.is_valid():
            task_entered=form_data.cleaned_data["task"]
            duration=form_data.cleaned_data["duration"]
                
            list_of_tasks.append(f"{task_entered}..............{duration} Mins")

            # list_of_tasks.append(data)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"tasks/addtask.html",{"form":form_data})
    
    return render(request,"tasks/addtask.html",{
            "form":NewTask()
        })

    