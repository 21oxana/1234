def read_data():
    with open('/Users/oxanarybkina/Desktop/GeekBrains/Python/Programming/Homeworks/After8Sem/fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def menu():
    print("Меню")
    print("1. Просмотр телефонной книги")
    print("2. Изменение данных")
    print("3. Запись новых данных")
    print("4. Выход")
    choice = input("Выберите действие: ")
    return choice

def change_data():
    print("Изменение данных")
    name = input("Введите имя контакта, чьи данные необходимо изменить: ")
    with open('/Users/oxanarybkina/Desktop/GeekBrains/Python/Programming/Homeworks/After8Sem/fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i in range(len(data)):
        if name in data[i]:
            newdata = input("Введите новые данные: ")
            data[i] = f"{name},{newdata}\n"
            with open('/Users/oxanarybkina/Desktop/GeekBrains/Python/Programming/Homeworks/After8Sem/fio.txt', 'w', encoding='utf-8') as file:
                file.writelines(data)
            print("Данные успешно изменены")
            return
    print("Контакт не найден")

def write_data():
    print("Запись новых данных")
    familia = input("Введите фамилию контакта: ")
    name = input("Введите имя контакта: ")
    otchev = input("Введите отчество контакта: ")
    phone = input("Введите номер телефона: ")
    with open('/Users/oxanarybkina/Desktop/GeekBrains/Python/Programming/Homeworks/After8Sem/fio.txt', 'r', encoding='utf-8') as file:
        file.write(f"{familia},{name},{otchev},{phone}")
    print("Данные успешно записаны")

def screen(data):
    print("Телефонная книга")
    for elem in data:
        print(elem.strip())

def main():
    # data = read_data()
    # screen(data)
    while True:
        choice = menu()
        if choice == "1":
            data = read_data()
            screen(data)
        elif choice == "2":
            change_data()
        elif choice == "3":
            write_data()
        elif choice == "4":
            break
        else:
            print("Неправильный выбор!")

if __name__ == '__main__':
    main()
