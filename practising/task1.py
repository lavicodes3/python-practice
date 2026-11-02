def listoverlap(a, b):
    set_a = set(a)
    set_b = set(b)
    in_both = sorted(set_a & set_b)
    in_one = sorted(set_a ^ set_b)
    return in_both, in_one

print(listoverlap([1, 2, 3, 4, 4], [3, 4, 5, 6]))