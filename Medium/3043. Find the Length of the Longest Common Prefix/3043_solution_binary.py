from bisect import bisect_left


class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        def commonPrefixLength(s1: str, s2: str) -> int:
            # Compare the two strings and find the common prefix length
            min_len = min(len(s1), len(s2))
            for i in range(min_len):
                if s1[i] != s2[i]:
                    return i
            return min_len

        # Convert all integers to strings for comparison
        str_arr1 = [str(x) for x in arr1]
        str_arr2 = [str(x) for x in arr2]

        # Sort the arrays of strings
        # Sorting helps because similar prefixes will be grouped together, which reduces the number of
        # comparisons needed to find the longest common prefix.
        str_arr1.sort()
        str_arr2.sort()

        # Initialize the longest common prefix length
        max_prefix_length = 0

        # Compare sorted arr1 and arr2 efficiently
        for s1 in str_arr1:
            # Use binary search to find the closest match for s1 in str_arr2
            # For each number in arr1, we use binary search to find the closest match in arr2,
            # avoiding the need to scan the entire arr2 array.
            idx = bisect_left(str_arr2, s1)

            # Check the current index and the previous one for a common prefix
            if idx < len(str_arr2):
                max_prefix_length = max(max_prefix_length, commonPrefixLength(s1, str_arr2[idx]))
            if idx > 0:
                max_prefix_length = max(max_prefix_length, commonPrefixLength(s1, str_arr2[idx - 1]))

        return max_prefix_length

    # Binary search reduces the number of comparisons by quickly narrowing down the search space,
    # making this approach faster for large input sizes.
