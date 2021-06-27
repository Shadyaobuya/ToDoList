from django.urls import path
from . import views

urlpatterns=[
    path("",views.hellow,name="Hello"),
    path("jayne",views.jayne,name="Jane"),
    path("<str:name>",views.greeting,name="Greeting")
]