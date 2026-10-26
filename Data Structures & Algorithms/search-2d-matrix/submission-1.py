class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mylist=[]
        
        for row in range(len(matrix)):
            if target <= matrix[row][-1]:
                matrix[row]
                l=0
                r=len(matrix[row])-1

                while l <= r:
                    mid = (l+r)//2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        r=mid-1
                    else:
                        l=mid+1
        return False


                