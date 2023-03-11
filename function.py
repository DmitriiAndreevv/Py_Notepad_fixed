import Note


def create_note(num):
    title = text_input(input('Введите название: '), num)
    body = text_input(input('Введите описание: '), num)
    return Note.Note(title=title, body=body)


def menu():
    print(
        "\t \n ЗАМЕТКИ \n \n Функционал\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер: ")


def text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символ \n')
        text = input('Введите текст: ')
    else:
        return text


def bye():
    print('До свидания!')
