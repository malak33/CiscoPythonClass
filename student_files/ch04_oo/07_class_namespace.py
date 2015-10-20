message = 'A global variable'


class MessageClass:
    message = 'Python classes are like namespaces'

    def __init__(self):
        print(message)

    for i in range(10):
        print(i, end='')
    print()
    print(message)

MessageClass()
