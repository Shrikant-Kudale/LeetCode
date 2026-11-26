class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]

            if h_left < h_right:
                if h_left >= left_max:
                    left_max = h_left
                else:
                    water += left_max - h_left
                left += 1
            else:
                if h_right >= right_max:
                    right_max = h_right
                else:
                    water += right_max - h_right
                right -= 1

        return water