from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.login_page,name='login'),
    path('mytasks/',views.my_tasks,name="index"),
    path('addtask/', views.addTask,name="addtask")
]