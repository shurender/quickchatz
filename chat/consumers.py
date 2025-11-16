import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WS USER =", self.scope["user"])

        self.room_code = self.scope["url_route"]["kwargs"]["room_code"]
        self.room_group_name = f"chat_{self.room_code}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        user = self.scope["user"]

        # lazy import models
        from .models import Message, ChatRoom

        # get room object
        room = await database_sync_to_async(ChatRoom.objects.get)(code=self.room_code)

        # save message
        await database_sync_to_async(Message.objects.create)(
            room=room,
            user=user,
            content=message
        )

        # broadcast
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": user.username
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        await self.send(text_data=json.dumps({
            "message": message,
            "user": user
        }))
