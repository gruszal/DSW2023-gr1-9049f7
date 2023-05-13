# więcej info tutaj: https://docs.python.org/3/library/typing.html#typing.Tuple
from typing import Union, List, Tuple, Optional


def prefix_names(prefix: str, items: Union[List[str], Tuple[str, ...]], postfix: Optional[str] = None) -> list:
    if postfix:
        return [f'{prefix}_{item}{postfix}' for item in items]
    else:
        return [f'{prefix}_{item}' for item in items]


if __name__ == '__main__':
    my_items = ('XXX', 'YYY')

    prefixed_items = prefix_names('new', my_items, '(temp)')
    print(prefixed_items)
