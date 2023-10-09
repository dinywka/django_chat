from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_app import models

admin.site.register(models.Room)
admin.site.register(models.Message)