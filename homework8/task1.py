def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        print(fd.read())


def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись, 2 - прочитать всю тел.книгу, 3 - изменить контакт, 4 - удалить контакт,  z - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            read_all(file)
        elif user_choice == '3':    
            update_contact(file)
        elif user_choice == '4':  
            delete_contact(file) 
        elif user_choice == 'z':
            print('Всего хорошего')
            break

def update_contact(f):
    name = input("Введите имя или фамилию контакта, который хотите изменить: ")
    new_phone = input("Введите новый номер телефона: ")
    
    with open(f, 'r', encoding='utf-8') as fd: 
        lines = fd.readlines()
    
    found = False
    
    with open(f, 'w', encoding='utf-8') as fd:
        for line in lines:
            if name.lower() in line.lower():
                fd.write(f"{line.split(':')[0]}: {new_phone}\n")
                found = True
            else:
                fd.write(line)
    
    if found:
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")

def delete_contact(f):
    name = input("Введите имя или фамилию контакта, который хотите удалить: ")
    
    with open(f, 'r', encoding='utf-8') as fd: 
        lines = fd.readlines()
    
    found = False
    
    with open(f, 'w', encoding='utf-8') as fd:
        for line in lines:
            if name.lower() not in line.lower():
                fd.write(line)
            else:
                found = True
    
    if found:
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

if __name__ == '__main__':
    main()