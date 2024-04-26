import unittest
from wkregister.decorator import record  # Import your decorator
from wkregister.models import Records
import asyncio


@record()
def add(a: float, b: float):

    record = Records(
        org="nmi",
        key="commonsense",
        userId="2",
        actionType="update",
        status="success",
        errorMessage=None,
        service="pay-service",
        payload={"hola": "mundo"},
    )
    return {"result": a + b, "record": record}


async def saveRecord():
    # Await the asynchronous method
    record = Records(
        org="commonsense",
        key="unittest",
        userId="2",
        actionType="update",
        status="success",
        errorMessage=None,
        service="pay-service",
        payload={"hola": "mundo"},
    )
    await record.save()


class TestLogs(unittest.TestCase):
    @unittest.skip
    def test_log(self):
        # Await the asynchronous method
        asyncio.run(add(12, 12))

        # Assert your test condition
        self.assertTrue(True)

    def test_register(self):
        # Await the asynchronous method
        record = Records(
            org="commonsense",
            key="unittest",
            userId="2",
            actionType="update",
            status="success",
            errorMessage=None,
            service="pay-service",
            payload={"hola": "mundo"},
        )

        asyncio.run(saveRecord())

        # Assert your test condition
        self.assertTrue(True)
