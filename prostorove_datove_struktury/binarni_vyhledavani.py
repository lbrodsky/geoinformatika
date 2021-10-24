#!/usr.bin/env python3

# binarni vyhledavani
# zdroj: MFF recepty z programátorské kuchařky


def bin_najdi(z):
    levy = 0
    pravy = N
    while levy <= pravy:
        median = (levy+pravy)/2
        # hledaná hodnota je vlevo
        if z < x[median]:
            pravy = median - 1
        # je vpravo
        elif z > x[median]:
            levy = median+1
            # našli jsme přímo hodnotu
        else:
            return median
        # hledaná hodnota nebyla nikde
        return -1

