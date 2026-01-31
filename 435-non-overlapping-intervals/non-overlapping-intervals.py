class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        pre = 0
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[pre][1]:
                pre = i
                count += 1
        return len(intervals) - count