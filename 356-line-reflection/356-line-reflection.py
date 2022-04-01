class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = set(map(tuple, points))
        
        point_min_x = min(points, key=lambda x: x[0])
        point_max_x = max(points, key=lambda x: x[0])
        
        middle_line = (point_min_x[0] + point_max_x[0]) / 2
        
        result = []
        for x, y in points:
            mirror_point = (2 * middle_line - x, y)
            result.append(mirror_point in points)
            
        return all(result)
            
            