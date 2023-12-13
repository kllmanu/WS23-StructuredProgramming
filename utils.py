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
