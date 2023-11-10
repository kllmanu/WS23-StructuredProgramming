import os

width, height = os.get_terminal_size()
divider = '-' * width

def test(fn, *args, **kwargs):
    print(divider)

    if fn.__doc__:
        print(fn.__doc__.split('\n')[0])
        print()

    result = fn(*args, **kwargs)

    if result is not None:
        print('  ', result)
