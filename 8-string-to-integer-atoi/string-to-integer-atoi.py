class Solution:
    def myAtoi(self, s: str) -> int:

        # # 
        
        # if negative:
        #     return -res

        # return res



        # res = 0
        # negative = False
        # for char in s:
        #     if char == " ":
        #         continue
        #     elif char == "-":
        #         negative = True
        #     elif char.isdigit():
        #         res = res * 10 + (ord(char))-ord('0')   # 0
        #     elif char.isalpha() and char == ".":
        #         break

        i = 0
        res = 0
        negative = False

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] == "-":
            negative = True
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        while i < len(s) and s[i].isdigit():
            res = res * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        if negative:
            res = -res

        if res < -2147483648:
            return - 2147483648
        elif res > 2147483647:
            return 2147483647
        
        return res
