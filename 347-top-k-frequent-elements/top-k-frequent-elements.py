class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # l = []
        # unique = set(nums)
        # for num in unique:
        #     l.append((nums.count(num),num))
        # print(l)
        # l.sort(reverse = True)
        # print(l)
        # res =[]
        # print(l[0][1]) 
        # for i in range(k):
        #     res.append(l[i][1])
        # return res

        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        sorted_ele = sorted(d.items(),key = lambda x:x[1],reverse = True)
        print(sorted_ele)
        return [sorted_ele[i][0] for i in range(k)]