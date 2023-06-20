
from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Channel_Room(models.Model):
    admin=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='admin')
    slug = models.SlugField(unique=True)
    bio=models.TextField(blank=True,max_length=10000)
    name=models.CharField(max_length=225)
    others=models.ManyToManyField(User, related_name='chs',blank=True)
    password=models.CharField(max_length=1000,blank=True)
    def __str__(self):
       return str(self.name)


class Channel_Member(models.Model):
    user=models.ForeignKey(User, related_name='user_channel', on_delete=models.CASCADE)
    rooms=models.ManyToManyField(Channel_Room, related_name='chrs',blank=True)
    def __str__(self):
       return str(self.user)

    def get_all_objects(self):
        return [f.user for f in self._meta.get_fields()]
        
class Slug(models.Model):
    data=models.IntegerField()#1000000
    def __str__(self):
       return str(self.id)
