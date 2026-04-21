class Memory:
    def __init__(self):
        self.state = {
            "intent": None,
            "name": None,
            "email": None,
            "platform": None
        }

    def update(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)
