def minExtraChar(s: str, dictionary: list) -> int:
    n = len(s)  # This is the total number of letters in the string `s`

    # We turn the dictionary into a set because it's faster to look up words in a set
    word_set = set(dictionary)

    # This is our DP table where dp[i] will tell us the smallest number of extra letters
    # we can have for the first `i` letters of the string `s`
    dp = [float('inf')] * (n + 1)  # Start with "infinity" (a very large number) for each spot
    dp[0] = 0  # If the string is empty (no letters), we have 0 extra letters

    # Now, we go through each letter in the string `s` one by one, like solving a puzzle
    for i in range(1, n + 1):
        # Assume that this letter is an extra letter by default
        dp[i] = dp[i - 1] + 1

        # Now we check if we can make a word from the dictionary ending at this letter
        for word in word_set:  # Look at each word in the dictionary
            word_len = len(word)  # How long is the word we are checking?

            # If the word can fit in the current place and matches the end of the string
            if i >= word_len and s[i - word_len:i] == word:
                # If the word matches, we update our dp array:
                dp[i] = min(dp[i], dp[i - word_len])  # No extra characters for this word!

    # Finally, dp[n] will tell us the minimum number of extra characters for the whole string
    return dp[n]


s = "leetscode"
dictionary = ["leet", "code", "leetcode"]

print(minExtraChar(s, dictionary))
