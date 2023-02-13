from django.urls import path

from . import views

urlpatterns = [
    path('', views.radiocomunicacao, name='radiocomunicacao'),
    path('mapa/', views.mapa, name='mapa'),
]
