# Number 1

class Rectangle:

    def __init__(self, a, b):

        self.square = Rectangle.square_rectangle(a, b)

    @staticmethod
    def square_rectangle(a, b):
        return a*b


p1 = Rectangle(3, 5)
p2 = Rectangle(4, 9)

print(p1.square, p2.square)

# Number 2

class Dog:
    count = 0

    def __new__(cls, *args, **kwargs):
        if Dog.count < 5:
            Dog.count += 1
            return super(Dog, cls).__new__(cls)



    def __init__(self, name, age, breed):

        self.name = name
        self.age = age
        self.breed = breed


a1 = Dog('a1', 1, 'rr')
a2 = Dog('a2', 2, 'rr')
a3 = Dog('a3', 3, 'rr')
a4 = Dog('a4', 4, 'rr')
a5 = Dog('a5', 5, 'rr')
a6 = Dog('a5', 6, 'rr')

print(id(a1), id(a2), id(a3), id(a4), id(a5), id(a6))
print(a1.name, a2.name, a3.name, a4.name)