class Singleton(object):
    def __new__(cls, value=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.value = value
        return cls.instance


class Singleton_second(object):
    def __new__(cls, value=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_second, cls).__new__(cls)
            cls.value = value
        return cls.instance


window = Singleton()
fullscreen = Singleton_second(False)
