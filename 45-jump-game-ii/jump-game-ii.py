class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0
        last_index = n - 1

        for i in range(last_index):
            reach = i + nums[i]
            if reach > farthest:
                farthest = reach

            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= last_index:
                    break

        return jumps