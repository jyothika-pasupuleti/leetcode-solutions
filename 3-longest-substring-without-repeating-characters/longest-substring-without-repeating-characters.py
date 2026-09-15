class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        start = 0
        right = 0
        longest = []
        max_len = 0
        for i in range(len(s)):
            while s[i] in longest:
                longest.remove(longest[0])
                left += 1
            longest.append(s[i])   #[c,a,b]   r = 5  l = 2
            right += 1

            if right - left > max_len:
                max_len = right - left
        return max_len
