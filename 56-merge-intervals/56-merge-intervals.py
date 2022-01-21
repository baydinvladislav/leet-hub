class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        merged_intervals = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if end >= interval[0]:
                end = max(interval[1], end)
            else:
                merged_intervals.append([start, end])
                start = interval[0]
                end = interval[1]

        merged_intervals.append([start, end])
        return merged_intervals