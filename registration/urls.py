""" school register URL Configuration"""
from django.views.generic import TemplateView
from django.urls import include
from django.urls import re_path
from .views import Register

urlpatterns = [
    re_path(
        r'^registration/success/$',
        TemplateView.as_view(template_name="registration/success.html"),
        name='register-success'),
    re_path(
        r'^registration/$',
        Register.as_view(),
        name='register'),
    re_path(
        r'^',
        include('django.contrib.auth.urls')),
]
