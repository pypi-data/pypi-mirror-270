from .int_to_int import int_to_int

def ienumerate(iterator, start=0, key=int_to_int):
    for i, v in enumerate(iterator, start):
        yield (key(i), v)
