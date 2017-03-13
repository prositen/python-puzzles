_lookup_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

from util.itertools import grouper


def to_base_64(string):
    r = []
    for grouped in grouper(string, 3, ""):
        t = "".join(grouped)
        b = "".join(['{:0>8}'.format(bin(ord(x))[2:]) for x in t]) + "0000"
        l = 6*len(t) + 1
        r.extend(_lookup_table[int(b[s:s+6], 2)] for s in range(0, l, 6))
    return "".join(r)


def from_base_64(string):
    r = []
    for grouped in grouper(string, 4, ""):
        b = "".join(['{:0>6}'.format(bin(_lookup_table.index(c))[2:]) for c in grouped])
        r.extend(chr(int(b[s:s+8], 2)) for s in range(0, 17, 8))
    return "".join(r).rstrip('\x00')
