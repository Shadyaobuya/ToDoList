from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.login_page,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_page,name='logout'),
    path('mytasks/',views.my_tasks,name="index"),
    path('addtask/', views.addTask,name="addtask"),
    path('home/', views.homepage,name='home')
]