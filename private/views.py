# from django.shortcuts import render
#
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
#
# from .models import Room, Message
#
# @login_required
# def pv_rooms(request):
#     privates = Room.objects.all()
#
#     return render(request, 'room/rooms.html', {'rooms': rooms})
#
# @login_required
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room)
#     string_without_spaces = str(request.user).replace(" ", "")
#     return render(request, 'room/room.html', {'room': room, 'messages': messages , 'user':string_without_spaces})
