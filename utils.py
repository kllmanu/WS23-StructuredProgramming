import os
from pprint import pprint

width, height = os.get_terminal_size()
divider = '-' * width
tested = []

def test(fn, *args, **kwargs):
    if fn.__doc__ and fn.__name__ not in tested:
        print(divider)
        print(fn.__doc__.split('\n')[0])

    print()

    result = fn(*args, **kwargs)

    if result is not None:
        pprint(result)

    tested.append(fn.__name__)


colors = {
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'darkcyan': '\033[36m',
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
}

formats = {
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reset': '\033[0m',
}
