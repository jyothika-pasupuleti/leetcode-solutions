class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for num in nums:
            if num != val:
                nums[pointer] = num
                pointer += 1
            
        return pointer
            
            