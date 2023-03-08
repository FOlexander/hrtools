from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_create_user, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)