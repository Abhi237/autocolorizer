
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepg),
    path('colorit/', views.colorpg, name='colored'),
    path('cont/', views.cont, name='contact')
]
