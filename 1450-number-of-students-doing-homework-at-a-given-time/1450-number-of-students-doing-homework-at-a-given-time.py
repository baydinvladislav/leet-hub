class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        pupils = 0
        for i in range(len(endTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                pupils += 1
        return pupils