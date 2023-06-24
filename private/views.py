from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Pv,IMG
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from django.http import JsonResponse

from .models import PV_Room, PV_Message,Slug,PV_Member

@login_required
def channel(request):
    return render(request, 'channel/channel_main.html',)
@login_required
def pv_rooms(request):

    us = User.objects.get(username=request.user)
    try:
        privates=[]
        for i in PV_Member.objects.get(user=us).others.all():
            privates.append(i)

        links=PV_Member.objects.get(user=us).others_rooms.all()
        list_link=[int(i.slug) for i in links]
    except:
        privates = []
        list_link=[]
        links=[]
    if request.method == 'POST':
        username = request.POST['username']
        tmp=User.objects.filter(username=username)
        if len(tmp):
            if tmp[0] in privates:
                for i in links:
                    if tmp[0]==i.user1 or tmp[0]==i.user2:
                        return redirect(f"/chat/{i.slug}/")
                a=links.index(tmp[0])
                return redirect(f"/chat/{links[a].slug}/")
                return HttpResponse(f"You had PV with {username}")
            
        slug = Slug.objects.get(id=1)
        if not User.objects.filter( username=username).exists():
            return HttpResponse("User not found.")
        use = get_object_or_404(User, username=username)
        use1 = User.objects.get( username=username)
        if use1==us:
            return HttpResponse("You can not make a private chat with your self.")
        slug.data+=1
        slug.save()
        us = User.objects.get(username=request.user)
        try:
            deu = PV_Member.objects.get(user=us)
            deu.others.add(use1)
            deu.save()
        except:
            deu = PV_Member(user=us)
            deu.save()
            deu.others.add(use1)
            deu.save()
        try:
            man = PV_Member.objects.get(user=use1)
            man.others.add(us)
            man.save()
        except:
            man = PV_Member(user=use1)
            man.save()
            man = PV_Member.objects.get(user=use1)
            man.others.add(us)
            man.save()

        New = PV_Room(user1=us, user2=use, slug=slug.data)
        New.save()
        deu.others_rooms.add(New)
        man.others_rooms.add(New)
        return redirect(f"/chat/{slug.data}/")
    else:
        form = Pv()
        linak=[]
        for i in links:
            if i.user1 == us:
                linak.append(i.user2.username)
            else:
                linak.append(i.user1.username)
        return render(request, 'pv_room/pvrooms.html', {'rooms': privates, 'form':form, 'links': list_link, 'len':len(list_link), "dav":linak })


def fetch_api(request):
    us = User.objects.get(username=request.user)
    try:
        user_channels=PV_Member.objects.get(user=us).channels.all()
        channel_link=[int(i.slug) for i in links]
    except:
        user_channels=[]
        channel_link=[]
    try:
        links=PV_Member.objects.get(user=us).others_rooms.all()
        list_link=[int(i.slug) for i in links]
        
    except:
        list_link=[]
        links=[]
    try:
        dislist=[]
        for i in privates:
            dislist.append(i.display_name)
    except:
    	dislist=[] 
    linak = []
    for i in links:
        if i.user1 == us:
            linak.append(i.user2.username)
        else:
            linak.append(i.user1.username)
    data={
        'links':list_link,
        'names':linak,
        'nul':len(list_link),
        'channel':user_channels,
        'link_channel':channel_link,
        'nuls':len(channel_link),
        'dislist':dislist,
        'dislen':len(dislist),
    }
    return JsonResponse(data)
def changer(old_path, id):
    from django.core.files.storage import default_storage
    old_path=old_path.split()
    new_path=f"{id}"+old_path[-1]
    default_storage.move(old_path, new_path)

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
def load(request,slug,img):
    return redirect("main_page")
