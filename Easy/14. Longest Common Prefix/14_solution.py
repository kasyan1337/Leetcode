# Solution script

def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Assume the first string is the common prefix
    prefix = strs[0]

    # Compare the assumed prefix with the rest of the strings
    for i in range(1, len(strs)):
        # Check the current string against the prefix
        while strs[i].find(prefix) != 0:
            # Shorten the prefix
            prefix = prefix[:-1]
            # If prefix becomes empty, return ""
            if not prefix:
                return ""

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
