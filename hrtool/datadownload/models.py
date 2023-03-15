from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PlotFile(models.Model):
    plot = models.ImageField(upload_to='uploads/', null=True)
    plot_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
