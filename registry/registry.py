from animals.animal import Animal
from animals.pets import Dog, Cat, Hamster
from animals.pack_animals import Horse, Camel, Donkey
import datetime

class Registry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal_type, name, birth_date):
        animal_classes = {
            'dog': Dog,
            'cat': Cat,
            'hamster': Hamster,
            'horse': Horse,
            'camel': Camel,
            'donkey': Donkey
        }
        animal_class = animal_classes.get(animal_type.lower())
        if not animal_class:
            print("Неизвестный тип животного!")
            return
        animal = animal_class(name, birth_date)
        self.animals.append(animal)
        print(f"{animal_type.capitalize()} по имени {name} добавлен в реестр.")

    def list_commands(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                print(f"Команды, которые знает {animal_name}: {animal.get_commands()}")
                return
        print(f"Животное по имени {animal_name} не найдено.")

    def teach_command(self, animal_name, command):
        for animal in self.animals:
            if animal.name == animal_name:
                animal.add_command(command)
                print(f"{animal_name} теперь знает команду: {command}")
                return
        print(f"Животное по имени {animal_name} не найдено.")

    def list_animals_by_birth_date(self):
        sorted_animals = sorted(self.animals, key=lambda animal: animal.birth_date)
        for animal in sorted_animals:
            print(f"{animal.name} ({animal.birth_date})")

    def get_total_animals(self):
        print(f"Общее количество животных: {Animal.get_total_animals()}")
