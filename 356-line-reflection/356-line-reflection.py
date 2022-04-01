class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = set(map(tuple, points))
        minx, _ = min(points, key=lambda x: x[0])
        maxx, _ = max(points, key=lambda x: x[0])
        rx = (minx + maxx) / 2

        result = []
        for x, y in points:
            point = (2 * rx - x, y)
            is_occurrencied = point in points
            result.append(is_occurrencied)

        return all(result)