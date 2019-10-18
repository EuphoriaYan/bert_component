# * - coding=utf-8 - * #

import os
import sys

import re
from collections import OrderedDict, MutableSet


class OrderedSet(OrderedDict, MutableSet):

    def update(self, *args, **kwargs):
        if kwargs:
            raise TypeError("update() takes no keyword arguments")

        for s in args:
            for e in s:
                 self.add(e)

    def add(self, elem):
        self[elem] = None

    def discard(self, elem):
        self.pop(elem, None)

    def __le__(self, other):
        return all(e in other for e in self)

    def __lt__(self, other):
        return self <= other and self != other

    def __ge__(self, other):
        return all(e in self for e in other)

    def __gt__(self, other):
        return self >= other and self != other

    def __repr__(self):
        return 'OrderedSet([%s])' % (', '.join(map(repr, self.keys())))

    def __str__(self):
        return '{%s}' % (', '.join(map(repr, self.keys())))

    difference = property(lambda self: self.__sub__)
    difference_update = property(lambda self: self.__isub__)
    intersection = property(lambda self: self.__and__)
    intersection_update = property(lambda self: self.__iand__)
    issubset = property(lambda self: self.__le__)
    issuperset = property(lambda self: self.__ge__)
    symmetric_difference = property(lambda self: self.__xor__)
    symmetric_difference_update = property(lambda self: self.__ixor__)
    union = property(lambda self: self.__or__)


if __name__ == '__main__':
    vocab = OrderedSet()
    comp = OrderedSet()

    with open("vocab.txt", "r", encoding="utf-8") as vocab_file:
        for line in vocab_file:
            l = line.rstrip()
            if l.startswith("#"):
                comp.add(l)
            else:
                vocab.add(l)

    pattern = re.compile('&[A-Z0-9-]+;')
    with open("chise-ids\\IDS-UCS-Basic.txt", "r", encoding="utf-8") as chaizi:
        chaizi.readline()
        for line in chaizi:
            l = line.rstrip().split('\t')
            vocab.add(l[1])
            c = l[2]
            if c == l[1]:
                continue
            f_list = re.findall(pattern, c)
            for f in f_list:
                comp.add("##" + f)
            re.sub(pattern, "", c)
            for f in c:
                comp.add("##" + f)

    with open("vocab2.txt", "w", encoding="utf-8") as vocab_file:
        for v in vocab:
            vocab_file.write(v + "\n")
        for c in comp:
            vocab_file.write(c + "\n")
