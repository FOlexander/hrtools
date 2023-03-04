from django.contrib import admin
from django.db import models
from .models import UploadedFile

# Register your models here.
admin.site.register(UploadedFile)