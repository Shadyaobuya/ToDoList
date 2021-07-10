from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=80, default="Shadya")
    password=models.CharField(max_length=80)

class login(models.Model):
    username=models.CharField(max_length=80, default="Shadya")
    password=models.CharField(max_length=80, default="Shadya")

