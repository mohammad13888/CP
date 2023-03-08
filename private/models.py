from django.db import models

from django.contrib.auth.models import User
from django.db import models

class PV_Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class PV_Message(models.Model):
    room = models.ForeignKey(PV_Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return str(self.id)
    class Meta:
        ordering = ('date_added',)
