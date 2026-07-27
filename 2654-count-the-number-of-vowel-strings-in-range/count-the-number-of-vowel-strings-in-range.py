class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """

        # v = "aeiouAEIOU"
        # c = 0
        # for i in range(left,right+1):
        #     if words[i][0] in v and words[i][-1] in v:
        #         c += 1
        
        # return c


        v = "aeiou"
        return sum(1 for i in range(left,right+1) if words[i][0] in v and words[i][-1] in v)


        