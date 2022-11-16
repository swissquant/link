from loguru import logger


class PubSub:
    def __init__(self):
        self.listeners_by_topic = {}

    def send(self, topic: str, message: dict, silent: bool = False):
        """
        Send a message to the listeners connected to the given topics
        """
        if topic in self.listeners_by_topic.keys():
            for listener in self.listeners_by_topic[topic]:
                listener.mailbox.post(message)

        if not silent:
            logger.info(f"{topic} - {message}")


pubsub = PubSub()
