# import math

# import gcd

# import math

# from math import factorial, acos

# from turtle import Turtle

import turtle

# from turtle import Turtle

# from collections import deque

import operator

import http.client

from math import sqrt

from fractions import Fraction

from gcd import gcd

x = type(dict().keys())


class test_class:
    def __init__(self):
        self.x = 0

    def add(self, num):
        self.x += num


class my_int(int):
    def trolol(self):
        pass


class my_dict(dict):
    pass


class my_super_int(my_int):
    pass


def main():

    list_ = [1, 2, 3]
    list_.count(5)

    gcd(5, 6)
    x = Fraction(5, 6)
    x.from_float(5.5)

    sqrt(10)

    list_ < [1, 2, 3, 5]

    dict_ = {1: 1, 2: 2, 3: 3}

    len(dict_)
    dict_.keys()

    list_of_lists = [[1, 2, 3], [2, 3, 4], [2, 3, 4]]

    list_of_lists == [[1, 2, 3], [2, 3, 4], [2, 3, 4]]

    x = "abcde"
    dict_ = {x: [1, 2, 3], 2: 2, (1, 2): 1}

    dict_ == {1: 1, 2: 2, 3: 3}

    x = dict_["abcde"]
    x = "Hello"
    x != "World"

    x = test_class()

    x.add(1)
    mydict = my_dict()
    mydict[0] = 0
    mydict[1] = 1

    1 in mydict

    x = my_super_int(1)
    x + my_super_int(2)
    x.trolol()


# main()

# testing_func()
