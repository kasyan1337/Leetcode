class Solution(object):
    def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        editable_list = list(nums)

        find_i = max(nums)
        editable_list.remove(max(nums))
        find_j = max(editable_list)

        return (find_j - 1) * (find_i - 1)


print(Solution.maxProduct([3, 4, 5, 2]))


# Leetcode Solutions

class Solution(object):
    def maxProduct(self, nums):
        max1 = float('-inf') # neg infinity
        max2 = float('-inf')

        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)

