class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, handler):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(handler)

    def unsubscribe(self, event, handler):
        if event in self.subscribers:
            self.subscribers[event].remove(handler)

    def publish(self, event, data):
        if event not in self.subscribers:
            return
        for handler in self.subscribers[event]:
            handler(data)


# Handlers
def email_service(data):
    print("Email sent:", data)

def analytics_service(data):
    print("Analytics logged:", data)


bus = EventBus()
bus.subscribe("USER_REGISTERED", email_service)
bus.subscribe("USER_REGISTERED", analytics_service)

bus.publish("USER_REGISTERED", "user@test.com")