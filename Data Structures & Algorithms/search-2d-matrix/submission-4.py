class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        for i in range(len(matrix)):
            if matrix[i][0] <= target: row=i
        left = 0
        right = len(matrix[0])-1
        while left<=right:
            mid = (left+right) // 2
            if matrix[row][mid] == target: return True
            elif matrix[row][mid] <= target: left=mid+1
            else: right = mid-1
        return False
        