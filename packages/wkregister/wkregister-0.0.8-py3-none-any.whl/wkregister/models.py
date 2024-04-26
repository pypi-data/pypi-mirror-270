from wkregister.producer import record2Kafka
from dataclasses import dataclass, field, asdict
from typing import Dict
import uuid
from datetime import datetime
import asyncio


@dataclass
class Records:
    org: str = ""
    key: str = ""
    userId: str = ""
    actionType: str = ""
    status: str = ""
    errorMessage: str = ""
    service: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=lambda: str(datetime.today()))
    payload: Dict = field(default_factory=dict)

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

    def kafkaParams(self):

        # Check if 'org' or 'key' was not set and inform the user
        if not self.org:
            print("Org was not set")
        if not self.key:
            print("Key was not set")

        # Return the extracted values
        return self.org, self.key

    def createRecord(self):
        return {
            "org": self.org,
            "key": self.key,
            "userId": self.userId,
            "actionType": self.actionType,
            "status": self.status,
            "errorMessage": self.errorMessage,
            "service": self.service,
            "id": self.id,
            "timestamp": self.timestamp,
            "payload": self.payload,
        }

    def validate(self):
        # Check if 'org' or 'key' was not set and inform the user
        if not self.org:
            print("Org was not set")
        if not self.key:
            print("Key was not set")

    async def save(self):

        self.validate()
        # Log after function execution, you can adjust what you log as needed
        asyncio.create_task(record2Kafka(self.org, self.key, self.createRecord()))
