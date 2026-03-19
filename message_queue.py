class MessageQueue:
    def __init__(self, retry_limit=2):
        self.queue = []
        self.dead_letter = []
        self.retry_limit = retry_limit

    def publish(self, message):
        self.queue.append({"data": message, "retries": 0})

    def process(self, handler):
        if not self.queue:
            print("No messages")
            return

        msg = self.queue.pop(0)

        success = handler(msg["data"])

        if not success:
            msg["retries"] += 1
            if msg["retries"] > self.retry_limit:
                self.dead_letter.append(msg)
                print("Moved to dead-letter queue:", msg["data"])
            else:
                self.queue.append(msg)


# Example handler
def worker(data):
    print("Processing:", data)
    return data != "fail"  # simulate failure


mq = MessageQueue()

mq.publish("task1")
mq.publish("fail")

for _ in range(5):
    mq.process(worker)