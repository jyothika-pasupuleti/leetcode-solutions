class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # for arr in matrix:
        #     low = 0
        #     high = len(arr)-1                  #  O(m log n)
        #     while low <= high:
        #         mid = (low+high) // 2
        #         if arr[mid] == target:
        #             return True
        #         elif arr[mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        # return False


        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid  + 1
            else:
                high = mid - 1
                
        return False





        