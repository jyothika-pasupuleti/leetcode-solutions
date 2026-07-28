class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ''
        c = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                c += 1
            else:
                if c > 1:
                    s += chars[i-1] + str(c)
                    c = 1
                else:
                    s += chars[i-1]
                    c = 1
        if c > 1:
            s += chars[-1] + str(c)
        else:
            s += chars[-1]
        print(s)
        for i in range(len(list(s))):
            chars[i] = s[i]
        
        return len(list(s))
            
