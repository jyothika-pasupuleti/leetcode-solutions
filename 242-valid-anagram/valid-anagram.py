class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if sorted(s) == sorted(t):
        #     return True
        # return False
        

        if len(s) != len(t):
            return False
        
        d = {}
        dd = {}
        for char in s:
            d[char] = d.get(char,0)+1
        for char in t:
            dd[char] = dd.get(char,0)+1
        
        if d == dd:
            return True
        return False

        # for char in t:
        #     if char not in d or d[char] == 0:
        #         return False
            
        #     d[char] -= 1

        # return True