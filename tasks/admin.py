from django.contrib import admin

# Register your models here.
from .models import login,signup

admin.site.register(login)
admin.site.register(signup)
