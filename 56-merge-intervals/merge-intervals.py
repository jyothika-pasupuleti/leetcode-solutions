class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        #print(intervals)
        res = [intervals[0]]

        for start,end in intervals[1:]:
            last_start,last_end = res[-1]
            if start <= last_end:
                res[-1][1] = max(last_end,end)
            else:
                res.append([start,end])
        return res

