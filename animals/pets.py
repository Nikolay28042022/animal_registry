from .animal import Animal

class Pet(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Dog(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Cat(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Hamster(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
