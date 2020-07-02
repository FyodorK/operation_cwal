

class Person:
    NUM = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    NUM = 0

    def create_person(self, name):
        t = Person(self.NUM, name)
        Person.NUM +=1
        return t


p = PersonFactory()

temp = p.create_person("Mark")
temp1 = p.create_person("Mark")
temp2 = p.create_person("Mark")

print(temp.id, temp.name)
print(temp1.id, temp1.name)
print(temp2.id, temp2.name)
