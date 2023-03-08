from django.contrib import admin

from .models import PV_Room
from .models import PV_Message

admin.site.register(PV_Room)
admin.site.register(PV_Message)