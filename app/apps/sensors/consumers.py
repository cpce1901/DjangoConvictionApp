import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from aiomqtt import Client, MqttError
from django.conf import settings
from urllib.parse import unquote


class MQTTConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.mqtt_task = asyncio.create_task(self.mqtt_listener())

    async def mqtt_listener(self):
        try:
            topic = self.scope['url_route']['kwargs']['topic']
            topic = str(topic).replace("-", "/")
            print(topic)

            async with Client(
                hostname=settings.MQTT_BROKER, 
                port=int(settings.MQTT_PORT), 
                username=settings.MQTT_USERNAME, 
                password=settings.MQTT_PASSWORD, 
                identifier=settings.MQTT_ID
                ) as client:

                await client.subscribe(topic)
                async for message in client.messages:
                    payload = message.payload.decode()
                    #print(f"Received MQTT message: {payload}")
                    await self.send(text_data=json.dumps({
                        'data_mqtt': payload
                    }))
        except MqttError as e:
            print(f"MQTT Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        

    async def disconnect(self, close_code):
        if hasattr(self, 'mqtt_task'):
            self.mqtt_task.cancel()
        print("WebSocket desconectado")

