#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Empowered:
    def __init__(self, a=0, b=0):
        self.first = float(a)
        self.second = float(b)

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._first = float(value)

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        self._second = float(value)

    def __str__(self):
        return f"{self.first} ^ {self.second}"

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        return self.first ** self.second

    def __add__(self, other):
        if isinstance(other, Empowered):
            first = self.first ** self.second
            second = other.first ** other.second
            summa = first + second
            return f"{first} + {second} = {summa}"

    def __sub__(self, other):
        if isinstance(other, Empowered):
            first = self.first ** self.second
            second = other.first ** other.second
            differ = first - second
            return f"{first} - {second} = {differ}"

    def __mul__(self, other):
        if isinstance(other, Empowered):
            first = self.first ** self.second
            second = other.first ** other.second
            multi = first * second
            return f"{first} * {second} = {multi}"

    def __truediv__(self, other):
        if isinstance(other, Empowered):
            first = self.first ** self.second
            second = other.first ** other.second
            quot = first / second
            return f"{first} / {second} = {quot}"

    def __eq__(self, other):
        if isinstance(other, Empowered):
            return (self.first == other.first) and \
            (self.second == other.second)
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Empowered):
            return not self.__eq__(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Empowered):
            return self.__float__() > other.__float__()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Empowered):
            return self.__float__() < other.__float__()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Empowered):
            return not self.__lt__(other)
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Empowered):
            return not self.__gt__(other)
        else:
            return False

    def __pow__(self):
        power = pow(self.first, self.second)
        print(f"{self.first} ^ {self.second} = {power}")
        return power


if __name__ == '__main__':
    r1 = Empowered(3, 3)
    r1.__str__()
    r1.__pow__()

    r2 = Empowered()
    r2.first = float(input("Введите первое число: "))
    r2.second = float(input("Введите второе число: "))
    r2.__pow__()

    print(r1.__ne__(r2))
    print(r1.__le__(r2))
    print(r2.__ge__(r1))

    S = r2.__add__(r1)
    M = r1.__mul__(r2)
    print(S, M, sep = "\n")

    r3 = Empowered(random.uniform(2, 10), random.uniform(1, 10))
    r3.__pow__()

    print(r3.__eq__(r1))
    print(r3.__gt__(r2))
    print(r3.__lt__(r1))

    D = r3.__sub__(r1)
    Q = r3.__truediv__(r2)
    print(D, Q, sep = "\n")