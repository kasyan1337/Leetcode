# Solution script

def twoSum(nums, target):
    # Create a dictionary to store numbers and their indices
    num_to_index = {}

    # Loop through the list to find the two numbers that add up to the target
    for i, num in enumerate(nums):
        # Calculate the complement that we need
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the complement and the current number
            return [num_to_index[complement], i]

        # Otherwise, store the current number and its index in the dictionary
        num_to_index[num] = i

    # This line will never be reached because the problem guarantees one solution
    return []


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
