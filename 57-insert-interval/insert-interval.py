class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # if not intervals:
        #     return [newInterval]
        # if len(intervals) == 1:  # [[1,5],[6,8]]
        #     res = [intervals[0]]
        #     if res[0][1] >= newInterval[0]:
        #         return [[min(res[0][0],newInterval[0]),max(res[0][1],newInterval[1])]]
        #     else:
        #         res.append(newInterval)
        #         return res

        # res = [intervals[0]]
        # for pair in intervals[1:]:
        #     if not res:
        #         res.append(intervals[0])
        #     first,last = res[-1][0],res[-1][1]  # 1,3
        #     if last >= newInterval[0]:
        #         res[-1][0],res[-1][1] = min(first,newInterval[0]),max(last,newInterval[1])
        #     else:
        #         res.append(newInterval)     #[1,5]
                
        #     x,y = pair
        #     if res[-1][1] >= x:
        #         res[-1][0],res[-1][1] = min(x,res[-1][0]),max(y,res[-1][1])
        #     else:
        #         res.append(pair)
        # return res



        res = []

        for interval in intervals:

            # 1. Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # 2. Current interval overlaps with newInterval
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

            # 3. Current interval is completely after newInterval
            else:
                res.append(newInterval)
                newInterval = interval

        # Add newInterval if it hasn't been added yet
        res.append(newInterval)

        return res
        