class Class:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'a:={self.a}\nb:={self.b}'

class Proto:
    @staticmethod
    def deep_copy(proto, *args):
        temp = __import__('copy').deepcopy(proto)
        for a in args:
            temp.a = a
        return temp


c = Class(1, 2)

d = Proto.deep_copy(c, 2, 3)

print(c)
print(d)

