class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(grid)
        cols = len(grid[0])
        new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        row_count = [grid[row].count(1) - grid[row].count(0) for row in range(rows)]
        col_count = [
            sum(grid[r][c] for r in range(rows)) - sum(1 - grid[r][c] for r in range(rows)) for c in range(cols)]

        for r in range(rows):
            for c in range(cols):
                new_matrix[r][c] = row_count[r] + col_count[c]

        return new_matrix


print(Solution.onesMinusZeros(None, [[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
print(Solution.onesMinusZeros(None, [[1, 1, 1], [1, 1, 1]]))


class Solution_leetcode(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n

        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]

        # Calculate the difference matrix
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n  # magical formula

        return grid


print(Solution_leetcode.onesMinusZeros(None, [[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
print(Solution_leetcode.onesMinusZeros(None, [[1, 1, 1], [1, 1, 1]]))
