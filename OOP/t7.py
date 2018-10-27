from importlib import import_module


def plugin_load(name: str, sep=':'):
    m, _, c = name.partition(sep)
    mod = import_module(m)
    cls = getattr(mod, c)
    return cls()


if __name__ == '__main__':
    # mod = __import__('t6')
    # cls = getattr(mod, 'A')
    cls = plugin_load('t6:A')
    cls.show_me()

