from datetime import datetime

def start_selection():
    print("\n" + "=" * 40)
    print('Вас приветствует приложение для заметок' + '!')
    print('Выберете действие с заметкой' + ':')
    print("\n" + "=" * 40)
    print('1 - добавить заметку '+';')
    print('2 - найти заметку по ID '+';')
    print('3 - найти заметку по дате ' +';')
    print('4 - редактировать заметку по ID '+';')
    print('5 - удалить заметку по ID '+';')
    print('6 - посмотреть все заметки '+ ';')
    print('7 - выйти из приложения '+ '.')
    command = int(input(": "))
    if 0 < command < 7:
        return command
    elif command == 7:
        return False
    else:
        print('используйте цифры от 1 до 7' + ',' + 'попробуйте ещё раз')


def confirm():
    print('Ваши заметки')


def create_note():
    title = input('введите заметку: ')
    data = input('введите описание: ')
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    note = {'title' : title, 'data': data, 'date': date}
    return note


def print_note(note):
    print(note['ID'])
    print(note['title'].center(20))
    print(note['data'])
    print(note['date'])
    print('-------------------')


def get_id():
    id = int(input('введите ID заметки: '))
    return id


def get_date():
    date = input('введите дату в формате дд.мм.гггг: ')
    return date


def not_find():
    print('Ваша заметка не найдена')