class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        special_elements_count = 0

        for prvy_list in range(len(mat)):  # beriem list
            for druhy_list in range(len(mat[prvy_list])):  # iterujem elementy v prvom liste
                if mat[prvy_list][druhy_list] == 1:  # Ci tam je je 1
                    if mat[prvy_list].count(1) == 1 and all(
                            mat[stlpec_check][druhy_list] == 0 for stlpec_check in range(len(mat)) if
                            stlpec_check != prvy_list):  # kuzlo
                        special_elements_count += 1

        return special_elements_count


print(Solution.numSpecial(None, [[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(Solution.numSpecial(None, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
