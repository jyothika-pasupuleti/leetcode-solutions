class Solution:
    def romanToInt(self, s: str) -> int:

        values = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}   
        
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                res -= values[s[i]]
            else:
                res += values[s[i]]
        
        return res
