from random import random


class RandomizedSet(object):

    def __init__(self):
        self.colls = {}
        self.lst = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.colls:
            return False
        self.lst.append(val)
        self.colls[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        try:
            ind = self.colls.pop(val)
            self.lst[ind], self.lst[-1] = self.lst[-1], self.lst[ind]
            self.lst.pop()
            self.colls[self.lst[ind]] = len(self.lst) - 1
            return True
        except (KeyError, IndexError):
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
