import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_index_map = {}
        self.index = -1
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_index_map:
            return False
        self.vals.append(val)
        self.index += 1
        self.val_index_map[val] = self.index
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_index_map:
            return False
        val_index = self.val_index_map[val]
        last_val = self.vals[-1]
        self.vals[val_index] = last_val
        self.val_index_map[last_val] = val_index
        self.vals.pop()
        del self.val_index_map[val]
        self.index -= 1
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()