from attr import define
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from pkg_resources import require
from .models import Channel_Member,Channel_Room, Slug
from django.contrib.auth.models import User
from .forms import Channel
from django.contrib import messages



def main_channels(request):
    if request.method == 'POST':
        id = request.POST.get('slug', '')
        password = request.POST.get('password', '')
        us = User.objects.get(username=request.user)
        userch=Channel_Member.objects.get(user=request.user)
        try:
            all_chs=Channel_Room.objects.get(slug=id)

        except:
            messages.error(
                request, f"ایدی یا گذرواژه نادرست است.")
            return redirect('/channel/')
        if all_chs.password == password and all_chs.slug == id:
            all_chs.others.add()
            userch.rooms.add(all_chs)
            all_chs.save()
            userch.save()
            messages.success(
                request, f"شما به کانال اضافه شدید.")
            return redirect(f"/channel/{all_chs.slug}/")

        else:
            messages.error(
                request, f"ایدی یا گذرواژه نادرست است.")
            return redirect('/channel/')

    else:
        form = Channel()
        userch=Channel_Member.objects.get_or_create(user=request.user)
        use=userch[0]
        links=use.rooms.all()
        list_link=[int(i.slug) for i in links]
        return render(request, 'channels_home.html',context={'form':form,'len':len(list_link),"roos": links, 'links':list_link})
def channel(request,slug):
    return render(request,'channelin.html' )