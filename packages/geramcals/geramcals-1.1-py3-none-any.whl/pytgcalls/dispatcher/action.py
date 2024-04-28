class Action:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.name
