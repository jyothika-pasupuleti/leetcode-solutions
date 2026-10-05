class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = strs[0]
        for word in strs[1:]:
            while not word.startswith(longest):
                longest = longest[:-1]
                if not longest:
                    return ""
        return longest
        