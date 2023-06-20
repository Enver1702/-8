


from phone_book import phone_book


def open_file(path: str = 'номера.txt'):
    phone_book.clear()
    file = open(path, 'r' , encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = ({ 'name' : nc[1], 'phone' : nc[2], 'comment': nc[3]})
        print('\nТелефонная книга успешно загружена!' )


def show_contacs(book: dict[int.dict]):
    print('\n' + '='*200)
    for i, cnt in book.items():
           print(f'{i:>3}, {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("contact"):<20}')
           print('='*200 + '\n')
           
def add_contact():
    uid = max(list(phone_book.keys())) + 1 
    
    name = input("Введите имя контакта: ") 
    phone = input("Введите телефрн контакта: ") 
    comment = input("Введите комментарий к контакту: ")   
    phone_book[uid] = {'name': name , 'phone': phone , 'comment': comment}      
    
def save_file():
    data= []
    for contact in phone_book.items():
        new = ':'.join([str('i')],[contact.get('name')],[contact.get('phone')],[contact.get('comment')])
        data.append(new)
        data = '\n'.join(data)
    with open( path , 'w' , encoding='UTF-8' )as file:
        file.write(data)
def search():
    result ={}
    word = input("Введите слово по которому будет осуществляться поиск: ")
    for i,contact in phone_book.items:
        if word.lower() in ''.join(list(contact.values())).lower():
            result[i] = contact
    return result

def remove():
    result = search()
    show_contacs(result)
    index = int(input("Введите ID контакта ,который хотите удалить : "))
    del_cnt = phone_book.pop(index)
    print(f'\nКонтакт{del_cnt.get("name")}успешно удален из книги:')
    print('=' * 200 + '\n')
    
def update(data):
    with open('/Enver/D:/MUSTANG/Программирование/python дз/ДЗ №8/номера.txt', 'w+') as newfile:
        newfile.writelines(data)


with open('/Enver/D:/MUSTANG/Программирование/python дз/ДЗ №8/номера.txt', 'r+') as file:
    file = file.readlines()
print(file)
while True:
    option = int(input('Выберите действие:\n1 - поиск ,2 - редактирование пользователя ,3 - добавление пользователя ,4 - удаление пользователя\n: '))
    if option == 1:
        search = input('Для поиска введите Фамилию (Имя), телефон: ')
        for i in file:
            if search in i:
                print(i)
    elif option == 2:
        search = input('Для редактирования введите Фамилию (Имя), телефон: ')
        for i in range(len(file)):
            if search in file[i]:
                print(file[i])
                option2 = str(input('Редактировать? Y/N: '))
                if option2 == 'Y':
                    file.remove(file[i])
                    add = input('Для редактирования введите Фамилию,Имя, Отчество, телефон пользователя: ')
                    file.insert(i, add + '\n')
                    update(file)
    elif option == 3:
        add = input('Для добавления введите Фамилию,Имя, Отчество, телефон пользователя: ')
        file.append(add + '\n')
        print(file)
        update(file)
    elif option == 4:
        search = input('Для удаления введите Фамилию (Имя), телефон: ')
        for i in range(len(file)):
            if search in file[i]:
                print(file[i])
                option2 = str(input('Удалить? Y/N: '))
                if option2 == 'Y':
                    file.remove(file[i])
                    update(file)
                    break
            
def menu() -> int:
    main_menu = '''Главное меню: 
    1. Открыть фаил.
    2. Cохранить фаил.
    3. Показать все контакты.
    4. Создать контакт.
    5. Найти контакт.
    6. Изменить контакт.
    7. Удалить контакт.
    8. Выход. '''
    print(main_menu)
    while True:
       select = input('выберите пункт меню: ')
       if select.isdigit() and 0 < int(select) < 9 :
           return int(select)
       print('Ошибка ввода, введите число от 1 до 8 : ')
    
while True:
    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            pass
        case 3:
            show_contacs(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacs(result)
        case 6:
            file()
        case 7:
            remove()
        case 8:
            print('До свидания,до новых встреч ')
            break
    