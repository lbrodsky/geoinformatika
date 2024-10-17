#!/usr/bin/env python3

# Jemny uvod do Python OOP (Object Oriented Programming)
# Cil: demonstrace teckove konvence pro atributy a metody trid Python

from math import sqrt

class Bod(object):
    """Trida Bod vraci souradnice objektu typu bod (x, y) 2D.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

# Vytvoreni instance objektu bod
mujbod = Bod(10.2, 13.7)
print(f'Typ objektu: {mujbod}')

# Ziskani atribut objektu: objekt tecka jmeno atributu
print(f'Souradnice x jako attribut: {mujbod.x}')
# Volani metody: objekt tecka jmeno metody se zavorkou
print(f'Souradnice x metodou get_x(): {mujbod.get_x()}')

#---

class DvaBody(Bod):
    """Trida DvaBody je konstruovana z tridy Bod, umi nest pouze dva body.
       Vraci bud bod a jeho atributy (souradnice) nebo pocita vzdalenost dvou bodu (metoda).
    """
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def get_distance(self):
        return sqrt((self.b1.x - self.b2.x)**2 + (self.b1.y - self.b2.y)**2)

# Instance tridy DvaBody
db = DvaBody(Bod(4,4), Bod(2,2))
# Volani metody pocitajici Eukleidovskou vzdalenost bodu
print(f'Vypocti vzdalenost dvou bodu metodou tridy: {db.get_distance()}')
