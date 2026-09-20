class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)-1):
        #     j = i
        #     pos = 1
        #     while j+1 < len(temperatures) and temperatures[j+1] <= temperatures[i]:  # got TLE
        #         j += 1
        #         pos += 1
        #     if j+1 < len(temperatures) and temperatures[j+1] > temperatures[i]:
        #         res[i] = pos
        # return res



        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return res
            
