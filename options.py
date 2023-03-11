import operations
import Note
import function

num = 6  # знаков минимум может быть в тексте заметки


def add():
    note = function.create_note(num)
    array = operations.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operations.record_file(array, 'a')
    print('Заметка добавлена.')


def show(text):
    logic = True
    array = operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('id: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет заметок.')


def change_or_delete_id(text):
    id = input('Введите id заметки: ')
    array = operations.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = function.create_note(num)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена.')
            if text == 'delete':
                array.remove(notes)
                print('Заметка удалена.')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Возможно, вы ввели неверный id')
    operations.record_file(array, 'a')
