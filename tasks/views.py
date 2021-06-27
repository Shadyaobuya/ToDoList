from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

 
# Create your views here.
list_of_tasks=[]

class NewTask(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",max_value=10,min_value=1)


def index(request):
    return render(request,'tasks/index.html',{
        "all_tasks":list_of_tasks
    })

def addTask(request):
    if request.method=="POST":
        form_data=NewTask(request.POST)
        if form_data.is_valid():
            task_entered=form_data.cleaned_data["task"]
            # priority_entered=form_data.cleaned_data["priority"]
            list_of_tasks.append(task_entered)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"tasks/addtask.html",{"form":form_data})
    
    return render(request,"tasks/addtask.html",{
            "form":NewTask()
        })

    