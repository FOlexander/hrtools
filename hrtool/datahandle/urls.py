from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('handle', views.handle, name='handle')
    # path('datadownloadc/', TemplateView.as_view(template_name="index.html")),
]