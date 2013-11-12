from weakref import WeakKeyDictionary

class EventManager(object):
    
    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def registerListener(self, listener):
        self.listeners[listener] = 1

    def unregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event):
        for listener in self.listeners.keys():
            listener.notify(event)
