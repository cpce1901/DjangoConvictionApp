import asyncio
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from asyncio_mqtt import Client, MqttError

class MQTTConsumer(AsyncConsumer):
    async def connect(self):
        self.mqtt_client = Client("broker.hivemq.com")  # Cambie esto por su broker MQTT
        self.should_run = True
        asyncio.create_task(self.mqtt_loop())

    async def mqtt_loop(self):
        while self.should_run:
            try:
                async with self.mqtt_client as client:
                    await client.subscribe("your/topic")
                    async for message in client.messages:
                        await self.handle_mqtt_message(message)
            except MqttError as error:
                print(f'MQTT error: {error}')
                await asyncio.sleep(5)  # Espera antes de intentar reconectar

    async def handle_mqtt_message(self, message):
        # Procesa el mensaje MQTT aquí
        print(f"Received message on topic {message.topic}: {message.payload}")
        # Puedes enviar el mensaje a través de WebSocket si es necesario
        await self.send({
            "type": "websocket.send",
            "text": message.payload.decode()
        })

    async def disconnect(self, close_code):
        self.should_run = False
        await self.mqtt_client.disconnect()
        raise StopConsumer()

    async def receive(self, text_data):
        # Maneja los mensajes recibidos del WebSocket
        # Por ejemplo, publica en un tema MQTT
        await self.mqtt_client.publish("your/publish/topic", text_data)