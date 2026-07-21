class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while n!= 0:
            temp = n % 2
            l.insert(0,temp)      #l.append(temp)  sometimes doesn't give accurate output
            n = n // 2

        for i in range(1,len(l)):
            if (l[i-1] == l[i]):
                return False
    
        return True
   
        