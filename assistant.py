USERS = {}


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except TypeError:
            result = 'Missing name or phone'
            print('Type')
        except UnboundLocalError:
            result = 'Unknown command'
            print('Unbound')
        return result
    return inner


def unknown_command(command: str) -> str:
    return f'Not command "{command}"'


def hello_user() -> str:
    return 'How can I help you?'


def exit_func() -> str:
    return 'Good buy!'


@input_error
def add_contact(name: str, phone: str) -> str:
    if name in USERS:
        return f'Contact Name: {name}, phone {USERS[name]} already exists'
    else:
        USERS[name] = phone
        return f'Contact Name: {name}, added phone {phone}'


@input_error
def change_phone(name: str, phone: str) -> str:
    old_phone = USERS[name]
    USERS[name] = phone
    return f'Contact Name: {name}, changed phone {old_phone} with a new {phone}'


@input_error
def show_contact(name: str) -> str:
    if name in USERS:
        result = f'Contact Name: {name}, phone: {USERS.get(name)}'
    else:
        result = f'Name: {name}, not in phone list'
    return result


@input_error
def show_all(all: str) -> str:
    if all in ('all', 'ALL', 'All'):
        result = 'Showing all contacts'
        if USERS.items():
            for name, phone in USERS.items():
                result += f'\nName: {name}, Phone: {phone}'
        else:
            result = 'No contacts, please add'
    return result


commands = {
    'hello': hello_user,
    'add': add_contact,
    'change': change_phone,
    'show': show_all,
    'phone': show_contact,
    'exit': exit_func,
    'goodbye': exit_func,
    'close': exit_func,
}


def main():
    while True:
        command, *data = input('Please enter request: ').strip().split(' ', 1)
        if commands.get(command.lower()):
            handler = commands.get(command.lower())
            if data:
                data = data[0].split(', ')
            result = handler(*data)
            if result == 'Good buy!':
                print(result)
                break
        else:
            result = unknown_command(command)
        print(result)


if __name__ == '__main__':
    main()
