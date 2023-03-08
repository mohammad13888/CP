from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import PV_Room, PV_Message

@login_required
def pv_rooms(request):
    privates = PV_Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': privates})

@login_required
def pv_room(request, slug):
    room = PV_Room.objects.get(slug=slug)
    messages = PV_Message.objects.filter(room=room)
    string_without_spaces = str(request.user).replace(" ", "")
    return render(request, 'room/room.html', {'room': room, 'messages': messages , 'user':string_without_spaces})
