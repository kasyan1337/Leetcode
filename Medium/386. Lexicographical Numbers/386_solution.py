def lexicalOrder(n: int):
    result = []

    # A helper function to perform DFS
    def dfs(current):
        # Base case: stop if the current number exceeds n
        if current > n:
            return

        # Add the current number to the result
        result.append(current)

        # Try to generate next numbers by multiplying by 10 (deeper in the tree)
        for i in range(10):
            next_number = current * 10 + i
            if next_number > n:
                break
            dfs(next_number)

    # Start DFS from 1 to 9
    for i in range(1, 10):
        if i > n:
            break
        dfs(i)

    return result