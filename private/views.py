from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Pv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect, HttpResponse

from .models import PV_Room, PV_Message,Slug,PV_Member

@login_required
def pv_rooms(request):
    all = PV_Member.objects.all()
    print(all, "\n\n\n\n")
    us = User.objects.get(username=request.user)
    print(us)
    try:
        privates = PV_Member.objects.get(user=us).others.all()
        print(privates)
        links=PV_Member.objects.get(user=us).others_rooms.all()
        list_link=[int(i.slug) for i in links]
    except:
        privates = []
        list_link=[]

    if request.method == 'POST':
        username = request.POST['username']
        us = User.objects.get(username=request.user)
        slug = Slug.objects.get(id=1)
        al=PV_Member.objects.all()

        use = get_object_or_404(User, username=username)
        use1 = User.objects.get( username=username)
        print(use1, "\n\n\n\n")
        slug.data+=1
        slug.save()

        us = User.objects.get(username=request.user)
        print(us)
        try:
            deu = PV_Member.objects.get(user=us)
        except:
            deu = PV_Member(user=us)
            deu.save()
        deu.others.add(use1)
        deu.save()
        New = PV_Room(user1=us, user2=use, slug=slug.data)
        New.save()
        deu.others_rooms.add(New)
        return redirect(f"/pv/{slug.data}/")
    else:
        form = Pv()

        return render(request, 'pv_room/pvrooms.html', {'rooms': privates, 'form':form, 'links': list_link, 'range':range(len(list_link)) })


@login_required
def room(request, slug):
    room = PV_Room.objects.get(slug=slug)
    messages = PV_Message.objects.filter(room=room)
    string_without_spaces = str(request.user).replace(" ", "")
    if request.user == room.user1 or request.user== room.user2:
        if request.user==room.user1:
            return render(request, 'pv_room/pvroom.html', {'room': room, 'messages': messages, 'user': string_without_spaces, "usa":room.user2})
        else:
            return render(request, 'pv_room/pvroom.html', {'room': room, 'messages': messages , 'user':string_without_spaces, "usa":room.user1})
    else:
        return HttpResponse("Access Denied")