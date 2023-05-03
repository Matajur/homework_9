USERS = {}


def unknown_command(_):
    return 'Unknown command'


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except NameError:
            result = (unknown_command, [])
            print('Name')
        except KeyError:
            result = 'Wrong name'
            print('Key')
        except ValueError:
            result = 'Give me name and phone please'
            print('Value')
        except IndexError:
            result = 'Enter user name'
            print('Index')
        except TypeError:
            result = 'Wrong type'
            print('Type')
        return result
    return inner


def hello_user(_):
    return 'How can I help you?'


def exit_func(_):
    return 'stop'


@input_error
def add_user(args):
    name, phone = args
    USERS[name] = phone
    return f'User {name} added!'


@input_error
def change_phone(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f'For user {name} old phone {old_phone} is changed with {phone}'


def show_all(_):
    result = ''
    for name, phone in USERS.items():
        result += f'Name: {name}, Phone: {phone}\n'
    result = result.removesuffix('\n')
    return result


def show_phone(args):
    result = f'Name: {args[0]}, Phone: {USERS.get(args[0])}'
    return result


HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'show all': show_all,
    'exit': exit_func,
    'good bye': exit_func,
    'close': exit_func,
    'phone': show_phone,
    'error': unknown_command
}


@input_error
def parse_input(user_input):
    command, *args = user_input.split(' ')
    command = command.lstrip()
    if args:
        if args[0] == 'all':
            command = command + ' all'
        elif args[0] == 'bye':
            command = command + ' bye'
    if command not in HANDLERS:
        raise NameError
    handler = HANDLERS[command.lower()]
    return handler, args


def main():
    while True:
        user_input = input('Please enter command and args (if any): ')
        main_command, *args = parse_input(user_input)
        result = main_command(*args)
        if result == 'stop':
            print('Good bye!')
            break
        print(result)


if __name__ == '__main__':
    main()
