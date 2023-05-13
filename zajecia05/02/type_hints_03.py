# więcej info tutaj: https://docs.python.org/3/library/typing.html#typing.Tuple
from typing import Union, List, Tuple


def prefix_names(prefix: str, items: Union[List[str], Tuple[str, ...]]) -> list:
    return [f'{prefix}_{item}' for item in items]


if __name__ == '__main__':
    my_items = ('XXX', 123)  # wartość int zadziała, ale nie jest przez nas oczekiwana

    prefixed_items = prefix_names('new', my_items)

    print(prefixed_items)
