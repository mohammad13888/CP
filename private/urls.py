

from . import views
from django.urls import path

urlpatterns = [
    path('', views.pv_rooms, name='pv_rooms'),
    path('fetch_api/', views.fetch_api, name='fetch-api'),
    path('channel/', views.channel, name='channel'),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/media/<str:img>', views.load, name='room'),
]