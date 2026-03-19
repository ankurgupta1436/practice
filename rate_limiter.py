class RateLimiter:
    def __init__(self, limit):
        self.limit = limit
        self.requests = {}  # user: count

    def allow_request(self, user):
        if user not in self.requests:
            self.requests[user] = 1
            return True

        if self.requests[user] < self.limit:
            self.requests[user] += 1
            return True

        return False

    def reset(self, user):
        self.requests[user] = 0


# Example
rl = RateLimiter(3)

user = "client_1"
for i in range(5):
    if rl.allow_request(user):
        print("Request allowed")
    else:
        print("Rate limit exceeded")
#(like API throttling systems) #Used in real systems to control request flow.