class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            small = matrix[m][0]
            large = matrix[m][-1]
            if target < small:
                r = m - 1
            elif target > large:
                l = m + 1
            else:
                l2, r2 = 0, len(matrix[m]) - 1
                while l2 <= r2:
                    m2 = (l2 + r2) // 2
                    val = matrix[m][m2]
                    if val < target:
                        l2 = m2 + 1
                    elif target < val:
                        r2 = m2 - 1
                    elif matrix[m][m2] == target:
                        return True
                return False
                    
        return False