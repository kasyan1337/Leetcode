class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
                ans -= dict[s[i]]
            else:
                ans += dict[s[i]]
        return ans

print(Solution.romanToInt("MCMXCIV"))