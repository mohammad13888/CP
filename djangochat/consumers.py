import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from private.models import PV_Room, PV_Message

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
        print(data)
        message = data['message']
        username = data['username']
        room = data['room']
        delete= data['delete']
        if delete==1:
            idd=await self.delete_message(username,room, message)
        else:
            iddd=await self.save_message(username, room, message)
        print("\n a request sent!!!")
        # Send message to room group
        if delete==0:

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'm_id':iddd

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
        m_id=event['m_id']
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'command':"add",
            'iddd':m_id
            
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
        PV_Message.objects.create(user=user, room=room, content=message)
        m=PV_Message.objects.get(user=user, room=room, content=message)
        return m.id

    @sync_to_async
    def delete_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = PV_Room.objects.get(slug=room)
        m=PV_Message.objects.get(id=message, user=user, room=room)
        i=m.id
        print(m)
        m.delete()
        return i


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