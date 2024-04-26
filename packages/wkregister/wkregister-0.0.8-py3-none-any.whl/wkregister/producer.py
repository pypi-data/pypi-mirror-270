import os
from confluent_kafka import Producer, KafkaException
from dotenv import load_dotenv
from typing import Dict
import json

load_dotenv()


producerconf = {
    "bootstrap.servers": os.getenv("BOOTSTRAP_SERVER"),
    "security.protocol": os.getenv("SECURITY_PROTOCOL"),
    "sasl.mechanisms": os.getenv("SASL_MECHANISM"),
    "sasl.username": os.getenv("SASL_USERNAME"),
    "sasl.password": os.getenv("SAS_PASSWORD"),
}


class KafkaProducerWrapper:
    def __init__(self):
        self.producer = Producer(producerconf)

    def get_producer(self):
        return self.producer


class KafkaMessageSender:
    def __init__(self, producer_wrapper):
        self.producer = producer_wrapper.get_producer()

    async def send(self, topic, key, value):
        def delivery_report(err, msg):
            if err is not None:
                print(f"Message not sent: {err}")
            else:
                # print(f'Message sent: {msg.value()}')
                print(f"Message sent")

        try:
            # Intenta enviar el mensaje
            self.producer.produce(topic, key=key, value=value, callback=delivery_report)
            self.producer.flush()  # Espera a que el mensaje se entregue
            return True  # Retorna True si se entregó exitosamente
        except KafkaException as e:
            print(f"Error sending to Kafka: {e}")
            return False  # Retorna False si ocurrió algún error


async def record2Kafka(org: str, key: str, value: Dict) -> None:
    producer_wrapper = KafkaProducerWrapper()
    # Crear el enviador de mensajes
    message_sender = KafkaMessageSender(producer_wrapper)
    # Enviar un mensaje
    topic = f"{org}_logs"
    key = f"{key}"
    value = json.dumps(value)
    await message_sender.send(topic, key, value)

    return None
