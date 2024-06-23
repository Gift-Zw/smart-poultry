import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("sensor_data", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("sensor_data", self.channel_name)

    async def send_data(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "sensor_data",
            {
                "type": "sensor_data_update",
                "data": data,
            }
        )
