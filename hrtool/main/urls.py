from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)