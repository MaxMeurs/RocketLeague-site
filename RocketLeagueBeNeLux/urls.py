from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('settings', views.settings, name='settings'),

    path('login', views.loginpage, name='login'),
    path('registreer', views.registeerpage, name='registreer'),
    path('logout', views.logoutusers, name='logout'),

    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name='BeNeLux/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name='BeNeLux/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='BeNeLux/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='BeNeLux/password_reset_done.html'),
         name='password_reset_complete'),
]