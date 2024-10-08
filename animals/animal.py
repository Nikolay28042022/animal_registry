class Animal:
    total_animals = 0  # общий счетчик для всех животных

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []
        Animal.total_animals += 1

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    @classmethod
    def get_total_animals(cls):
        return cls.total_animals
