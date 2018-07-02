# https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = list()
        self.map = dict()
        random.seed()

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            if self.val_list[self.map[val]]:
                res = False
            else:
                res = True
            self.val_list[self.map[val]].append(val)
        else:
            self.val_list.append([val])
            self.map[val] = len(self.val_list) - 1
            res = True
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map and self.val_list[self.map[val]]:
            self.val_list[self.map[val]].pop(-1)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        tmp_list = []
        for l in self.val_list:
            tmp_list.extend(l)

        n = len(tmp_list) - 1
        x = random.randint(0, n)
        return tmp_list[x]
