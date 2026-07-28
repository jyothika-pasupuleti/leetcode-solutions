class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # s = ''
        # c = 1
        
        # for i in range(1,len(chars)):
        #     if chars[i] == chars[i-1]:
        #         c += 1
        #     else:
        #         if c > 1:
        #             s += chars[i-1] + str(c)
        #             c = 1
        #         else:
        #             s += chars[i-1]
        #             c = 1

        # if c > 1:
        #     s += chars[-1] + str(c)
        # else:
        #     s += chars[-1]
        
        # for i in range(len(list(s))):
        #     chars[i] = s[i]
        
        # return len(s)
            

        pointer = 0
        n = len(chars)
        i = 0

        while i < n:
            count = 1
            char = chars[i]
            while i+1 < n and chars[i] == chars[i+1]:
                count += 1
                i += 1
            chars[pointer] = char
            pointer += 1

            if count > 1:
                for digit in str(count):
                    chars[pointer] = digit
                    pointer += 1

            i += 1

        return pointer

