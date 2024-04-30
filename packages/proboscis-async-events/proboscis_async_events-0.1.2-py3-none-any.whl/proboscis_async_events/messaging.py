import asyncio
from dataclasses import dataclass, field

import pampy


@dataclass
class Subscriber:
    src_handle: "Messages"
    messages: asyncio.Queue = field(default_factory=asyncio.Queue)

    async def tell(self, message):
        await self.messages.put(message)

    async def get(self):
        ev = await self.messages.get()
        return ev

    def unsubscribe(self):
        self.src_handle.unsubscribe(self)

    def __aiter__(self):
        return self

    async def __anext__(self):
        item = await self.get()
        if item is None:
            raise StopAsyncIteration
        return item

    async def wait(self, pattern):
        from pampy import _
        matched = False
        while not matched:
            message = await self.get()

            def on_match(*args):
                nonlocal matched
                matched = True

            pampy.match(message,
                        pattern, on_match,
                        _, lambda *args: None
                        )
        return message


@dataclass
class Messages:
    subscribers: list[Subscriber] = field(default_factory=list)

    def subscribe(self) -> Subscriber:
        subscriber = Subscriber(self)
        self.subscribers.append(subscriber)
        return subscriber

    async def publish(self, message):
        for subscriber in self.subscribers:
            await subscriber.tell(message)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    async def close(self):
        await self.publish(None)
