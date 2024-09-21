class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_set = set(s)
        t_set = set(t)
        diff = s_set.difference(t_set)
        diff_backwards = t_set.difference(s_set)

        if len(t) != len(s):
            return False

        s_list = list(s)
        t_list = list(t)

        for si in s_list:
            if s_list.count(si) != t_list.count(si):
                return False

        if len(diff) == 0 and len(diff_backwards) == 0:
            return True


# print(Solution.isAnagram(None, "anagram", "nagaram"))
# print(Solution.isAnagram(None, "rat", "car"))
# print(Solution.isAnagram(None, "a", "ab"))  # false
# print(Solution.isAnagram(None, "aa", "a"))  # false
# print(Solution.isAnagram(None, "aacc", "ccac"))  # false



class leetcode_Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        char_map = [0] * 26

        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_map)


print(leetcode_Solution.isAnagram(None, "anagram", "nagaram"))
print(leetcode_Solution.isAnagram(None, "rat", "car"))
print(leetcode_Solution.isAnagram(None, "a", "ab"))  # false
print(leetcode_Solution.isAnagram(None, "aa", "a"))  # false
print(leetcode_Solution.isAnagram(None, "aacc", "ccac"))  # false