import time
import re

front = """Що я вмію?\n
    Список моїх команд нижче:\n
    add - Створення нового контакту\n
    change [ім'я] - Змінює контакт\n
    phone [ім'я] - Показує номер телефону вибраного користувача\n
    all - Показує телефонну книгу\n
    help - виводить список команд\n
    close/exit - Припинити роботу помічника"""
def start():
    print("Привіт! Я твій персональний бот-помічник!")
    time.sleep(3)
    print(front)
    chose()


contacts = {}


def add():
    global contacts
    user_names = input("Введіть ім*я :").strip().lower()
    user_phones = input("Введіть телефон :").strip()
    if check_number(user_phones):
        if user_names in contacts:
            print("Це ім'я вже існує")
        else:
            contacts[user_names] = user_phones
            print("Контак додано!")
            print(contacts)
            return chose()
    else:
        print("Номер телефону в неправильному форматі")


def check_number(user_phones):
    pattern = re.compile(r"^\+\d{3}\s?\d{2}\s?\d{7}$")
    if pattern.match(user_phones):
        return bool(pattern.match(user_phones))


def chose():
    while True:
        pick_command = input("Введіть бажану дію >>> ")
        if pick_command in ['add', 'change', 'phone', 'all', 'help', 'close', 'exit']:
            if pick_command == "add":
                add()
            elif pick_command == "change":
                change()
            elif pick_command == "phone":
                phone()
            elif pick_command == "all":
                all()
            elif pick_command == "help":
                help()
            elif pick_command == 'close':
                print("Бай")
                break
            elif pick_command == 'exit':
                print("Бай")
                break
        else:
            print("Введіть значення з функціоналу:")


def change():
    global contacts
    name = input("Введіть ім'я контакту, який хочете змінити: ").strip().lower()

    if name in contacts:
        print(f"Зараз номер для {name}: {contacts[name]}")
        new_phone = input(f"Введіть новий номер телефону для {name}: ").strip()

        if check_number(new_phone):
            contacts[name] = new_phone
            print("Номер телефону оновлено.")
            print(contacts)
        else:
            print("Номер телефону в неправильному форматі")
    else:
        print("Такого імені немає в контактах.")
        add_choice = input("Чи хочете ви додати новий контакт? (так/ні): ").strip().lower()
        if add_choice == 'так':
            add()


def phone():
    global contacts
    name = input("Введіть ім'я контакту, який Ви хочете переглянути: ").strip().lower()
    if name in contacts:
        print(f"{contacts[name]}")
    else:
        print("Такого контакту не знайдено")
        return chose()


def all():
    global contacts
    if contacts:
        for name, phone in contacts.items():
            print(f"{name} {phone}")
    else:
        print("Ваша телефонна книга порожня")
        add_choice = input("Чи хочете ви додати новий контакт? (так/ні): ").strip().lower()
        if add_choice == 'так':
            add()

def help():
    print(front)

if __name__ == "__main__":
    start()



