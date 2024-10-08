from .animal import Animal

class PackAnimal(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Horse(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Camel(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Donkey(PackAnimal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
