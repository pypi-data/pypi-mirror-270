class WrapperBase:
    __slots__ = '__dict__'

    def __repr__(self):
        return f'<{self.__class__.__name__}>({vars(self)})'

    def __str__(self):
        return repr(self)
