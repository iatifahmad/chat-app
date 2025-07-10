
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Message
from asgiref.sync import sync_to_async

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.target_email = self.scope['url_route']['kwargs']['email']
        self.user = self.scope['user']
        self.target_user = await sync_to_async(User.objects.get)(email=self.target_email)
        self.room_name = f"chat_{min(self.user.id, self.target_user.id)}_{max(self.user.id, self.target_user.id)}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        previous_messages = await self.get_previous_messages()
        for msg in previous_messages:
            await self.send(text_data=json.dumps(msg))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print(f"Received message: {message} from {self.user.email} to {self.target_user.email}")
        msg_obj = await self.save_message(self.user, self.target_user, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg_obj.content,
                'sender': self.user.email,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))

    @sync_to_async
    def save_message(self, sender, receiver, message):
        return Message.objects.create(sender=sender, receiver=receiver, content=message)

    @sync_to_async
    def get_previous_messages(self):
        return [
            {
                'message': msg.content,
                'sender': msg.sender.email,
            }
            for msg in Message.objects.filter(
                sender__in=[self.user, self.target_user],
                receiver__in=[self.user, self.target_user]
            ).order_by('timestamp')
        ]