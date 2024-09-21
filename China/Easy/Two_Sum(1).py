class leetcode(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):  ## range moze prijat 3 argumenty range(start, stop, step)
                if i != y and nums[i] + nums[y] == target:
                    return [i, y]


print(leetcode.twoSum([2, 7, 11, 15], 9))
