from random import randrange

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        pos = self.pos
        if val not in pos:
            return False

        nums = self.nums
        idx = pos.pop(val)
        last_val = nums.pop()

        if idx < len(nums):
            nums[idx] = last_val
            pos[last_val] = idx

        return True

    def getRandom(self):
        nums = self.nums
        return nums[randrange(len(nums))]