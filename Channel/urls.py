from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_channels, name='main_channels'),
    path('<slug:slug>/', views.channel, name='channels'),

]