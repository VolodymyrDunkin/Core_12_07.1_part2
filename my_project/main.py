import sys

from .func import cool_func

def greeting():
    print("Hello world")


def greeting_name(name=None):
    if not name:
        try:
            name = sys.argv[1]
            print(f"Hello {name}")
        except IndexError:
            greeting()
    else:
        print(f"Hello {name}")