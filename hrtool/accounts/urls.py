from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.my_create_user, name='create'),
    path('password_reset/',  auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/',  auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)