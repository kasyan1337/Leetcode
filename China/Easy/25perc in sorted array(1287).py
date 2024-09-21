class Solution(object):
    def findSpecialInteger(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        percentage = 0.25 * len(arr)
        most_frequent = 0

        for i in arr:
            if arr.count(i) > arr.count(most_frequent):
                most_frequent = i

        if arr.count(most_frequent) >= percentage:
            return most_frequent


print(Solution.findSpecialInteger([6700, 8858, 8858, 8858, 8858]))


# class Solution(object):
#     def findSpecialInteger(self, arr):
#         size = len(arr)
#         qtr = size // 4
#         cnt = 1
#         p = arr[0]
#
#         for i in range(1, size):
#             if p == arr[i]:
#                 cnt += 1
#             else:
#                 cnt = 1
#
#             if cnt > qtr:
#                 return arr[i]
#
#             p = arr[i]
#
#         return p

