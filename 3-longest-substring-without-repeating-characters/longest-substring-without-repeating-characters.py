class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = set()
        max_len = 0
        for i in range(len(s)):
            while s[i] in longest:
                longest.remove(s[left])
                left += 1
            longest.add(s[i])   #[c,a,b]   r = 5  l = 2
            right += 1

            if right - left > max_len:
                max_len = right - left
        return max_len
