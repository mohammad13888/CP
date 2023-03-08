from django.urls import path

from . import views

urlpatterns = [
    path('', views.pv_rooms, name='pv_rooms'),
    path('<slug:slug>/', views.pv_room, name='room'),
]