class Field:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __str__(self):
        return "type: {} name: {}".format(self.type, self.name)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = {}
        self.margin = 2

    def __str__(self):
        s = "class {}:\n".format(self.name)
        if self.fields:
            s += " " * self.margin + "def __init__(self):\n"
            for t, n in self.fields.items():
                s += " " * 2 * self.margin + 'self.{} = {}\n'.format(t, n)
        else:
            s += " " * self.margin + 'pass'
        return s


class CodeBuilder:
    def __init__(self, root_name):
        self.root = Class(root_name)

    def add_field(self, type, name):
        __f = Field(type, name)
        self.root.fields[__f.type] = __f.name
        return self

    def __str__(self):
        return self.root.__str__()


if __name__ == '__main__':
    cb = CodeBuilder('Person')#.add_field('name', '""').add_field('age', '0')
    print(cb)


