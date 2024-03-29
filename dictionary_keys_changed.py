#Code returns a list of the 5 latest changed dictionary keys
class HistoryDict:
    def __init__(self, szotar):
        self.szotar = szotar
        self.list_of_changed_keys = []

    def set_value(self, new_value, additional):
        for key in list(self.szotar.keys()):
            self.szotar[new_value] = self.szotar.pop(key)

    def get_history(self):
        for key in self.szotar.keys():
            self.list_of_changed_keys.append(key)
        if len(self.list_of_changed_keys) <= 5:
            print(self.list_of_changed_keys)
            return self.list_of_changed_keys
        elif len(self.list_of_changed_keys) > 5:
            print(self.list_of_changed_keys[-5:])
            return self.list_of_changed_keys[-5:]
        else:
            print(self.list_of_changed_keys)
            return self.list_of_changed_keys

d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()

d.set_value("foo", 44)
d.get_history()
