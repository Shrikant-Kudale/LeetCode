class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n

        candies = 1
        up = 0
        down = 0
        peak = 0

        for i in range(1, n):
            prev, curr = ratings[i - 1], ratings[i]

            if prev < curr:
                up += 1
                down = 0
                peak = up
                candies += 1 + up
            elif prev == curr:
                up = 0
                down = 0
                peak = 0
                candies += 1
            else:
                up = 0
                down += 1
                candies += 1 + down - (1 if peak >= down else 0)

        return candies