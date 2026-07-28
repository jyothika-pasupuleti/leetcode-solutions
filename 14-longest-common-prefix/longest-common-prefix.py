class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs:
        #     return ""
        
        # prefix = strs[0]

        # for i in range(len(prefix)):
        #     for word in strs[1:]:
        #         if i >= len(word) or prefix[i] != word[i]:         # brute force
        #             return prefix[:i]

        # return prefix        


        if not strs:
            return ""
        strs.sort()
        print(strs)

        first = strs[0]
        last = strs[-1]

        # for i in range(len(first)):
        #     if i >= len(last) or first[i] != last[i]:        # using for loop
        #         return first[:i]
        
        # return first


        i = 0
        while i < len(first) and first[i] == last[i]:          # using while loop
            i += 1

        return first[:i]  