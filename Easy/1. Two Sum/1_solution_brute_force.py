# Solution script

def twoSum(nums, target):
    # Outer loop iterates through each element in the array
    for i in range(len(nums)):
        # Inner loop iterates through each element after i
        for j in range(i + 1, len(nums)):
            # Check if the current pair adds up to the target
            if nums[i] + nums[j] == target:
                return [i, j]
    # No need for an explicit return if a solution is guaranteed


# Example 1:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

# Example 2:
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]

# Example 3:
nums = [3, 3]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]
