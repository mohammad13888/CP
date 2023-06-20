import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import os
from django.conf import settings
from private.models import PV_Room, PV_Message,Slug
import base64

class PV_ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from Socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        command = data['command']
        if command=='message_no_file':
            message = data['message']
            username = data['username']
            room = data['room']
            msg=await self.save_message(username, room, message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'm_id':msg.id,
                    'm_message':msg.content

                }
            )
        elif command=='file_included_message':
            message = data['message']
            username = data['username']
            room = data['room']
            msg=await self.save_message(username, room, message)
            await self.file_included_message(data['file'],msg)
        elif command=='edit':
            message = data['message']
            id = data['id']
            room = data['room']
            edited=await self.edit_message(id,room,message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_edit',
                    'message': edited[0].content,
                    'username': edited[1],
                    'm_id': edited[0].id,
                    'm_message': edited[0].content

                }
            )
        elif command=='delete':
            username = data['username']
            room = data['room']
            message = data['message']
            deleted=await self.delete_message(username,room, message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'delete_meessage',
                    'message__id':deleted,
                    'username': username,
                }
            )
    # Receive message from room group

    async def file_included_message(self, file_data,obj):
        file_type = file_data['name']
        dot_index = file_type.rfind('.')
        suffix = file_type[dot_index:]
        file_name = str(obj.id) + suffix
        object = await self.file_allow(obj, file_name)
        obj=object[0]
        file_content = file_data['content']
        file_path = os.path.join(settings.MEDIA_ROOT, str(file_name))
        file_content = base64.b64decode(file_content.split(',')[1])
        with open(file_path, 'wb') as file:
            file.write(file_content)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'file_message',
                'file_name':file_name,
                'message': obj.content,
                'username': object[1],
                'iddd': obj.id,
                'm_message': obj.content
            }
        )
    async def file_message(self,event):
        message = event['message']
        username = event['username']
        file_name=event['file_name']
        iddd=event['iddd']
        m_message=event['m_message']
        await self.send(text_data=json.dumps({
            'command': 'file_message',
            'file_name': file_name,
            'message':message,
            'username':str(username),
            'iddd': iddd,
            'm_message':m_message
        }))
    async def chat_edit(self, event):
        message = event['message']
        username = str(event['username'])
        m_id = event['m_id']
        m_message = event['m_message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'command': "edit",
            'edited_id': m_id,
            'm_message': m_message

        }))
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        m_id=event['m_id']
        m_message=event['m_message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'command':"add",
            'iddd':m_id,
            'm_message':m_message


        }))
    async def delete_meessage(self, event):
        message = event['message__id']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message__id': message,
            'username': username,
            'command':"del"
        }))
    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = PV_Room.objects.get(slug=room)
        dif= Slug.objects.get(id=2)
        dif.data+=1
        dif.save()
        PV_Message.objects.create(user=user,dif=dif.data, room=room, content=message,edited=0)
        m=PV_Message.objects.get(user=user, room=room, content=message,dif=dif.data)
        return m
    @sync_to_async
    def delete_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = PV_Room.objects.get(slug=room)
        m=PV_Message.objects.get(id=message, user=user, room=room)
        i=m.id
        print(m)
        m.delete()
        return i
    @sync_to_async
    def edit_message(self, id, room, message):
        room = PV_Room.objects.get(slug=room)
        m=PV_Message.objects.get(id=id, room=room)
        m.content=message
        m.edited=1
        m.save()
        return m,m.user
    @sync_to_async
    def file_allow(self,obj,file_name):
        obj.file=file_name
        obj.save()
        return obj,obj.user












"""

import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from room.models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from Socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']
        delete = data['delete']
        if delete == 1:
            idd = await self.delete_message(username, room, message)
        else:
            iddd1 = await self.save_message(username, room, message)
        print("\n a request sent!!!")
        # Send message to room group
        if delete == 0:

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'm_id': iddd1

                }
            )
        else:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'delete_meessage',
                    'message__id': idd,
                    'username': username,
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        m_id = event['m_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'command': "add",
            'iddd': m_id

        }))

    async def delete_meessage(self, event):
        message = event['message__id']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message__id': message,
            'username': username,
            'command': "del"

        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=message)
        m = Message.objects.get(user=user, room=room, content=message)
        return m.id

    @sync_to_async
    def delete_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        m = Message.objects.get(id=message, user=user, room=room)
        i = m.id
        print(m)
        m.delete()
        return i
"""
