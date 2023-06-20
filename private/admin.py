from django.contrib import admin

from .models import PV_Room, PV_Message,Slug,PV_Member, Channel_Room,Channel_Message

admin.site.register(PV_Room)
admin.site.register(PV_Message)
admin.site.register(Channel_Room)
admin.site.register(Channel_Message)
admin.site.register(PV_Member)
admin.site.register(Slug)