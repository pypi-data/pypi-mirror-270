from .chr_to_int import chr_to_int
from .int_to_chr import int_to_chr

def irange(start, stop=None, step=None, index=0, numbers="abcdefghijklmnopqrstuvwxyz"):
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
    start, stop, step = fix_args_position(start, stop, step)

    try:
        return int_range(start, stop, step)
    except Exception:
        pass

    try:
        return str_range(start, stop, step, index=index, numbers=numbers)
    except Exception:
        pass


def int_range(start, stop, step):
    start = 0 if start is None else int(start)
    stop = int(stop)
    step = fix_step(start, stop, step)
    return range(start, stop, step)


def str_range(start, stop, step, index, numbers):
    start = numbers[0] if start is None else str(start)
    start = chr_to_int(start, start=index, numbers=numbers)
    stop = str(stop)
    stop = chr_to_int(stop, start=index, numbers=numbers)
    step = fix_step(start, stop, step)
    for i in range(start, stop, step):
        yield int_to_chr(i, start=index, numbers=numbers)


def fix_args_position(start, stop, step):
    step = 1 if step is None else int(step)
    if stop is None:
        return None, start, step
    return start, stop, step


def fix_step(start, stop, step):
    step = abs(step)
    if stop < start:
        step = step * -1
    return step

