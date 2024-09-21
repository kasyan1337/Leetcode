class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs or "" in strs:
            return ""
        elif len(strs) == 1:
            return strs[0]

        shortest_str = min(strs, key=len)

        for i in range(len(shortest_str)):
            if not all(s[i] == shortest_str[i] for s in strs):
                return shortest_str[:i]

        return shortest_str


print(Solution.longestCommonPrefix(["ab", "a"]))
