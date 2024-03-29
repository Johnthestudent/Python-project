from datetime import datetime
class Field:
    __value = None
    def __init__(self):
        self.__value = None
    # Code does a full_encapsulation
    def get_value(self):
        if self._value is None:
            self._value = datetime.datetime.now()
        return self._value

    def set_value(self, new_value):
        self._value = new_value

    value = property(get_value, set_value)
