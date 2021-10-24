#!/usr/bin/env python3

# B-strom
# src: https://www.programiz.com/dsa/b-tree
# TODO: https://pythontutor.com/visualize.html#mode=edit


# Vytvor uzel
class BStromUzel:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Vytvor B-strom
class BStrom:
    def __init__(self, t):
        self.root = BStromUzel(True)
        self.t = t

    # vypis strom
    def vypis_strom(self, x, l=0):
        print("Patro ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.vypis_strom(i, l)

    # Hledej klic
    def hledej_klic(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.hledej_klic(k, x.child[i])
        else:
            return self.hledej_klic(k, self.root)

    # Vloz klic
    def vloz_klic(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BStromUzel()
            self.root = temp
            temp.child.vloz_klic(0, root)
            self.rozdel(temp, 0)
            self.vloz_non_full(temp, k)
        else:
            self.vloz_non_full(root, k)

    # Vloz non 
    def vloz_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.rozdel(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.vloz_non_full(x.child[i], k)

    # Rozdel 
    def rozdel(self, x, i):
        t = self.t
        y = x.child[i]
        z = BStromUzel(y.leaf)
        x.child.vloz_klic(i + 1, z)
        x.keys.vloz_klic(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]


def main():
    B = BStrom(3)

    for i in range(10):
        B.vloz_klic((i, 2 * i))

    B.vypis_strom(B.root)

    if B.hledej_klic(8) is not None:
        print("\nNalezen")
    else:
        print("\nNenalezen")


if __name__ == '__main__':
    main()
