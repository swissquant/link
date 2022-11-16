from .pubsub import pubsub
from .mailbox import Mailbox


class Listener:
    def __init__(self, topics: list = []):
        self.mailbox = Mailbox()

        for topic in topics:
            self.subscribe(topic=topic)

    def subscribe(self, topic: str):
        """
        Subscribe to a given topic
        """
        if topic not in pubsub.listeners_by_topic.keys():
            pubsub.listeners_by_topic[topic] = []

        pubsub.listeners_by_topic[topic].append(self)

    async def pop_msg(self):
        """
        Wait for the next message and extract it
        """
        await self.mailbox.wait()
        return self.mailbox.pop_msg()
