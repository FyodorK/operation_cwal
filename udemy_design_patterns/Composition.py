class SingleValue:
    def __init__(self, value):
        self.value = value

    @property
    def sum(self):
        return sum([self.value])

    def get(self):
        return self.value


class ManyValues(list):
    def __init__(self):
        super().__init__()

    @property
    def sum(self):
        temp = 0
        t = [i.get() if isinstance(i, SingleValue) else i for i in self]
        for i in t:
            if isinstance(i, list):
                temp += sum(i)
            else:
                temp += i
        return temp


if __name__ == '__main__':
    a = SingleValue(11)
    b = ManyValues()
    b.append(22)
    b.append(33)
    c = ManyValues()
    c.append(a)
    c.append(b)
    print(f'{c.sum}')
