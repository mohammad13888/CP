from django.db import models

from django.contrib.auth.models import User
from django.db import models

class PV_Room(models.Model):
    user1=models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    user2=models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    def __str__(self):
       return str(self.id)

class PV_Message(models.Model):
    room = models.ForeignKey(PV_Room, related_name='pv_room', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='pv_sender', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return str(self.id)
    class Meta:
        ordering = ('date_added',)


class Slug(models.Model):
    data=models.IntegerField()#1000000
    def __str__(self):
       return str(self.id)

class PV_Member(models.Model):
    a=User.objects.get(username="moh")
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    others=models.ManyToManyField(User, related_name='pvs',blank=True)
    others_rooms=models.ManyToManyField(PV_Room, related_name='pvrs',blank=True)
    def __str__(self):
       return str(self.user)

    def get_all_objects(self):
        return [f.user for f in self._meta.get_fields()]
