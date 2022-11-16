import asyncio


class Mailbox:
    def __init__(self):
        self.messages = []
        self.event = asyncio.Event()

    def post(self, message):
        """
        Post a message and signal it
        """
        # Adding the message to the mailbox
        self.messages.append(message)

        # Signaling there are new messages
        self.event.set()
        self.event.clear()

    def pop_msg(self):
        """
        Pop the first message out of the mailbox
        """
        return self.messages.pop(0)

    async def wait(self):
        """
        Wait for the next message to be posted
        """
        if len(self.messages) == 0:
            await self.event.wait()
