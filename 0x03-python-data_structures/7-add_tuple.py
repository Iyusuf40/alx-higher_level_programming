#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        a, b = tuple_a
    elif len(tuple_a) == 1:
        a, b = tuple_a[0], 0
    else:
        a, b = 0, 0

    if len(tuple_b) >= 2:
        x, y = tuple_b
    elif len(tuple_b) == 1:
        x, y = tuple_b[0], 0
    else:
        x, y = 0, 0

    a = a + x
    b = b + y
    return (a, b)
#    if len(tu#ple_a) >= 2 and len(tuple_b) >= 2:
#        first#_mem = tuple_a[0] + tuple_b[0]
#        sec_m#em = tuple_a[1] + tuple_b[1]
#        new_t#uple = first_mem, sec_mem
#        retur#n new_tuple
#    elif len(#tuple_a) == 1 and len(tuple_b) == 1:
#        first#_mem = tuple_a[0] + tuple_b[0]
#        sec_m#em = 0
#        new_t#uple = first_mem, sec_mem
#        return new_tuple
#    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
#        first_mem = tuple_a[0] + tuple_b[0]
#        sec_mem = tuple_a[1]
#        new_tuple = first_mem, sec_mem
#        return new_tuple
#    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
#        first_mem = tuple_a[0] + tuple_b[0]
#        sec_mem = tuple_a[2]
#        new_tuple = first_mem, sec_mem
#        return new_tuple
#    elif len(tuple_a) >= 1 and len(tuple_b) == 0:
#        return tuple_a
#    elif len(tuple_a) == 0 and len(tuple_b) >= 1:
#        return tuple_b
#    else:
#        return (0,0)


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
