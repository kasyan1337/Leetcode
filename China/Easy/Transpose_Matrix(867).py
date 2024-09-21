class Solution(object):
    def transpose(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # solution = []
        # if len(matrix) == 3:
        #     solution.append([matrix[0][0], matrix[1][0], matrix[2][0]])
        #     solution.append([matrix[0][1], matrix[1][1], matrix[2][1]])
        #     solution.append([matrix[0][2], matrix[1][2], matrix[2][2]])
        # elif len(matrix) == 2:
        #     solution.append([matrix[0][0], matrix[1][0]])
        #     solution.append([matrix[0][1], matrix[1][1]])
        #     solution.append([matrix[0][2], matrix[1][2]])
        # elif len(matrix) == 1:
        #     solution.append([matrix[0][0]])
        #
        # return solution

        row = len(matrix)
        col = len(matrix[0])
        result = [[0] * row for _ in range(col)]

        for c in range(col):
            for r in range(row):
                result[r][c] = matrix[c][r]

        return result


print(Solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
