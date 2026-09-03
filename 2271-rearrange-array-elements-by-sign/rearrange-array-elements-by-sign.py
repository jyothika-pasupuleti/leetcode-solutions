class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])
        index=0
        for i in range(len(nums)//2):
            nums[index] = positives[i]
            index += 1
            nums[index] = negatives[i]
            index += 1
            
        return nums



