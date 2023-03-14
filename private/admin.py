from django.contrib import admin

from .models import PV_Room, PV_Message,Slug,PV_Member

admin.site.register(PV_Room)
admin.site.register(PV_Message)
admin.site.register(PV_Member)
admin.site.register(Slug)