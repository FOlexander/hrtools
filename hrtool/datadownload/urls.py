from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.download_view, name='dload')
    # path('datadownloadc/', TemplateView.as_view(template_name="index.html")),
]