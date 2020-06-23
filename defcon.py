from abc import ABC, ABCMeta, abstractmethod


class Bar(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def change_gear(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass


class Foo(Bar):

    def __init__(self, ma, mo, co ):
        self.ma = ma
        self.mo = mo
        self.co = co


if __name__ == '__main__':


    for x in range(1,10):
        for y in range(1,10):
            a = x * 10 + y
            b = x + y * 10
            if a == 4.5 * b:
                print(x, y)
