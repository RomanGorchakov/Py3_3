#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Decimal:
    def __init__(self, a=1, b=1):
        self.signed = int(a)
        self.unsigned = int(a) + (1 << 32)

        self.size = b
        num = [int(item) for item in range(1, b + 1)]

        max_size = 100
        max_num = [int(item) for item in range(1, max_size + 1)]

    @property
    def unsigned(self):
        return self._unsigned

    @unsigned.setter
    def unsigned(self, value):
        self._unsigned = int(value) + (1 << 32)

    def __str__(self):
        return f"{self._unsigned}"

    def __repr__(self):
        return self.__str__()

    def signed(self):
        return self.signed

    def __add__(self, other):
        if isinstance(other, Decimal):
            first = int(self.signed)
            first_u = first + (1 << 32)
            second = int(other.signed)
            second_u = second + (1 << 32)
            summa = first + second
            summa_u = summa + (1 << 32)
            return f"{first_u} + {second_u} = {summa_u}"

    def __sub__(self, other):
        if isinstance(other, Decimal):
            first = int(self.signed)
            first_u = first + (1 << 32)
            second = int(other.signed)
            second_u = second + (1 << 32)
            summa = first - second
            summa_u = summa + (1 << 32)
            return f"{first_u} - {second_u} = {summa_u}"

    def __mul__(self, other):
        if isinstance(other, Decimal):
            first = int(self.signed)
            first_u = first + (1 << 32)
            second = int(other.signed)
            second_u = second + (1 << 32)
            summa = first * second
            summa_u = summa + (1 << 32)
            return f"{first_u} * {second_u} = {summa_u}"

    def __truediv__(self, other):
        if isinstance(other, Decimal):
            first = int(self.signed)
            first_u = first + (1 << 32)
            second = int(other.signed)
            second_u = second + (1 << 32)
            summa = first - second
            summa_u = summa / (1 << 32)
            return f"{first_u} / {second_u} = {summa_u}"

    def __eq__(self, other):
        if isinstance(other, Decimal):
            return (self.signed == other.signed)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Decimal):
            return not self.__eq__(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Decimal):
            return self.signed > other.signed
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Decimal):
            return self.signed < other.signed
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Decimal):
            return not self.__lt__(other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Decimal):
            return not self.__gt__(other)
        else:
            return False

    def show(self):
        print(f"unsigned int {self.signed} = {self._unsigned}")
        return self.signed, self._unsigned


if __name__ == '__main__':
    r1 = Decimal(4, 10)
    r1.__str__()
    r1.show()

    r2 = Decimal()
    r2.signed = int(input("Введите число: "))
    r2.size = int(input("Введите размер числа: "))
    r2.show()

    print(r1.__ne__(r2))
    print(r1.__le__(r2))
    print(r2.__ge__(r1))

    S = r2.__add__(r1)
    M = r1.__mul__(r2)
    print(S, M, sep = "\n")

    r3 = Decimal(random.randint(1, 100), 10)
    r3.__str__()
    r3.show()

    print(r3.__eq__(r1))
    print(r3.__gt__(r2))
    print(r3.__lt__(r1))

    D = r3.__sub__(r1)
    Q = r3.__truediv__(r2)
    print(D, Q, sep = "\n")