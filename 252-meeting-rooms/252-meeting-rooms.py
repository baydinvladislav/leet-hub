from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        start, end = 0, 1

        for i in range(1, len(intervals)):
            if intervals[i - 1][end] > intervals[i][start]:
                return False
        return True
    