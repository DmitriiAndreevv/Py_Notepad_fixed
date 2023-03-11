import options as func
import function


def run():
    input_from_user = ''
    while input_from_user != '7':
        function.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            func.show('all')

        if input_from_user == '2':
            func.add()

        if input_from_user == '3':
            func.show('all')

            func.change_or_delete_id('delete')
        if input_from_user == '4':
            func.show('all')

            func.change_or_delete_id('edit')
        if input_from_user == '5':
            func.show('date')

        if input_from_user == '6':
            func.show('id')
            func.change_or_delete_id('show')
            
        if input_from_user == '7':
            function.bye()
            break
