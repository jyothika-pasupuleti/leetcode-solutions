class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        for i in range(rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    v = res[i-1][j-1] + res[i-1][j]
                    temp.append(v)

            res.append(temp)
        return res[-1]

                    
                    