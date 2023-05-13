# jakie dane przyjmuje poniższa funkcja?

def prefix_names(prefix, items):
    return [f'{prefix}_{item}' for item in items]


if __name__ == '__main__':
    my_items = ['XXX', 'YYY']

    prefixed_items = prefix_names('new', my_items)

    print(prefixed_items)
