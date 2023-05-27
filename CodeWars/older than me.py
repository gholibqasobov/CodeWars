class Person:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def compare_ages(self, p):
        # print(getattr(p, 'age'))
        if self.age == getattr(p, 'age'):
            print(getattr(p, 'name'), 'is the same age as me.')
        elif self.age < getattr(p, 'age'):
            print(getattr(p, 'name'), 'is older than me')
        else:
            print(getattr(p, 'name'), 'is younger than me')

p1 = Person('John', 19)
p2 = Person('Hey', 44)

p1.compare_ages(p2)
