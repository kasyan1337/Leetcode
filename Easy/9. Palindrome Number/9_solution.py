def isPalindrome(x: int) -> bool:
    # If x is negative, it's not a palindrome
    if x < 0:
        return False
    # Convert x to string and check if it reads the same backward
    return str(x) == str(x)[::-1]


# Example usage
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))  # Output: False
