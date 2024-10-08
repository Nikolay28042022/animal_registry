from registry.registry import Registry
from utils.helpers import parse_birth_date

def main():
    registry = Registry()
    while True:
        print("\nМеню:")
        print("1. Добавить новое животное")
        print("2. Показать список команд животного")
        print("3. Обучить животное новой команде")
        print("4. Показать список животных по дате рождения")
        print("5. Показать общее количество животных")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            animal_type = input("Введите тип животного (dog, cat, hamster, horse, camel, donkey): ").lower()
            name = input("Введите имя животного: ")
            birth_date_input = input("Введите дату рождения (YYYY-MM-DD): ")
            birth_date = parse_birth_date(birth_date_input)
            if birth_date:
                registry.add_animal(animal_type, name, birth_date)

        elif choice == '2':
            animal_name = input("Введите имя животного: ")
            registry.list_commands(animal_name)

        elif choice == '3':
            animal_name = input("Введите имя животного: ")
            command = input("Введите команду для обучения: ")
            registry.teach_command(animal_name, command)

        elif choice == '4':
            registry.list_animals_by_birth_date()

        elif choice == '5':
            registry.get_total_animals()

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
