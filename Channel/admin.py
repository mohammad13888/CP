from django.contrib import admin
from django.forms import SlugField
from .models import Channel_Member,Channel_Room,Slug
# Register your models here.
admin.site.register(Channel_Room)
admin.site.register(Channel_Member)
admin.site.register(Slug)
