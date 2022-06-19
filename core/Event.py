_callbacks = {}


class Event:

    @staticmethod
    def on(event_name, f):
        _callbacks[event_name] = _callbacks.get(event_name, []) + [f]
        return f

    @staticmethod
    def emit(event_name, *data):
        [f(*data) for f in _callbacks.get(event_name, [])]

    @staticmethod
    def off(event_name, f):
        _callbacks.get(event_name, []).remove(f)