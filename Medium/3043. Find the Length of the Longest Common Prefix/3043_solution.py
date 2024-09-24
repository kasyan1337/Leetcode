# Solution script
def longestCommonPrefixLength(arr1, arr2):
    def common_prefix_len(str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if str1[i] != str2[i]:
                return i
        return min_len

    arr1_str = list(map(str,arr1))
    arr2_str = list(map(str,arr2))

    max_prefix_len = 0

    for num1 in arr1_str:
        for num2 in arr2_str:
            prefix_len = common_prefix_len(num1,num2)
            max_prefix_len = max(max_prefix_len,prefix_len)
    return max_prefix_len


# Example 1:
arr1 = [1, 10, 100]
arr2 = [1000]
print(longestCommonPrefixLength(arr1, arr2))  # Output: 3

# Example 2:
arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(longestCommonPrefixLength(arr1, arr2))  # Output: 0