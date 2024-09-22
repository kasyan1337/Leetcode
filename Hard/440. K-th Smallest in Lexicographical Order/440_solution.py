class Solution:
    def findKthNumber(self, n: int, k: int) -> int:  # Add 'self' as the first parameter
        # A helper function to calculate the number of steps between cur and cur + 1
        def count_steps(n, cur, next):
            steps = 0
            while cur <= n:
                steps += min(n + 1, next) - cur
                cur *= 10
                next *= 10
            return steps

        cur = 1
        k -= 1  # We start from 1, so we reduce k by 1

        while k > 0:
            steps = count_steps(n, cur, cur + 1)
            if steps <= k:
                # If k is larger than the steps between cur and cur+1, move to next sibling
                cur += 1
                k -= steps
            else:
                # Else go deeper in the current tree
                cur *= 10
                k -= 1

        return cur