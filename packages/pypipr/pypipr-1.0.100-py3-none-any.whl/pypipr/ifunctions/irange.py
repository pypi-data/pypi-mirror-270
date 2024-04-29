from ..ibuiltins.chr_to_int import chr_to_int
from ..ibuiltins.int_to_chr import int_to_chr


def irange(start, stop=None, step=1, index=0, numbers="abcdefghijklmnopqrstuvwxyz"):
    """
    Meningkatkan fungsi range() dari python untuk pengulangan menggunakan huruf

    ```python
    print(irange('a', 'c'))
    print(irange('z', 'a', 10))
    print(list(irange('a', 'z', 10)))
    print(list(irange(1, '7')))
    print(list(irange(10, 5)))
    ```
    """
    if stop is None:
        stop = start
        start = 0

    if isinstance(start, int) and isinstance(stop, int):
        return range(start, stop, step)

    elif isinstance(start, str) and isinstance(stop, str):
        return char_range(start, stop, step, index=index, numbers=numbers)

    else:
        raise Exception("start dan stop tidak diketahui")


def char_range(start, stop, step, numbers, index):
    start = chr_to_int(start, start=index, numbers=numbers)
    stop = chr_to_int(stop, start=index, numbers=numbers)

    for i in range(start, stop, step):
        yield int_to_chr(i, start=index, numbers=numbers)


