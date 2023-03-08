from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.download_view, name='dload')
    # path('datadownloadc/', TemplateView.as_view(template_name="index.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)