from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ContactConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("contacts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("contacts", self.channel_name)

    async def contact_update(self, event):
        await self.send(text_data=json.dumps(event["content"]))
