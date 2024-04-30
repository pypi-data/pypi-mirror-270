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
        start = numbers[0] if isinstance(start, str) else 0

    step = 1 if step is None else int(step)

    try:
        return range(int(start), int(stop), step)
    except Exception:
        pass

    if isinstance(start, str) and isinstance(stop, str):
        return char_range(start, stop, step, index=index, numbers=numbers)

    raise Exception("start dan stop berbeda tipe")


def char_range(start, stop, step, numbers, index):
    start = chr_to_int(start, start=index, numbers=numbers)
    stop = chr_to_int(stop, start=index, numbers=numbers)

    for i in range(start, stop, step):
        yield int_to_chr(i, start=index, numbers=numbers)
