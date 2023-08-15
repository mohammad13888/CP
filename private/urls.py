from . import views
from django.urls import path

urlpatterns = [
    path('', views.main_chat, name='main_chat'),
    path('start/', views.pv_rooms, name='pv_rooms'),
    path('fetch_api/', views.fetch_api, name='fetch-api'),
    path('channel/', views.channel, name='channel'),
    path('channel/invite/<slug:slug>/', views.channel_invite, name='channel_invite'),
    path('channel/<slug:slug>/', views.channel_room, name='channel_room'),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/media/<str:img>', views.load, name='room'),
]