from channels.generic.websocket import AsyncwebsocketConsumer
import json

class ChatRoomConsumer(AsyncwebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name   ']
        self.room_group_name = 'userchat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'tester_message',
                'tester':'this is ajay',
            }
        )

    async def tester_message(self,event):
        tester = event['tester']

        await self.send(text_data=json.dumps({
            'tester': tester,
        }))

    async def disconnect(self,close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

