class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)

        if str(x_str) == str(x_str[::-1]):
            return True
        else:
            return False


print(Solution.isPalindrome(-121))
