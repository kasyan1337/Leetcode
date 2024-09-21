class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        outgoing_cities = []
        has_route = []

        for i in range(len(paths)):
            for j in range(len(paths[i])):
                outgoing_cities.append(paths[i][len(paths[i]) - 1])

        for i in range(len(paths)):
            if paths[i][0] in outgoing_cities:
                has_route.append(paths[i][0])

        destination_city = set(outgoing_cities).difference(has_route)

        return destination_city.pop()


print(Solution.destCity(None, [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(Solution.destCity(None, [["B", "C"], ["D", "B"], ["C", "A"]]))
print(Solution.destCity(None, [["A", "Z"]]))

print(Solution.destCity(None, [["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]))


class leetcode_solution(object):
    def destCity(self, paths):

        cities = set()

        for path in paths:
            cities.add(path[0])

        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest


print(leetcode_solution.destCity(None, [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
print(leetcode_solution.destCity(None, [["B", "C"], ["D", "B"], ["C", "A"]]))
print(leetcode_solution.destCity(None, [["A", "Z"]]))

print(leetcode_solution.destCity(None, [["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]))
