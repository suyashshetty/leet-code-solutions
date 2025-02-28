from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        # Helper function: Count number of elements <= x in the matrix.
        def countLessEqual(x):
            count = 0
            # Start from the bottom-left corner.
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    # All elements in current row above the current row are <= x.
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        # Binary search boundaries.
        left, right = matrix[0][0], matrix[-1][-1]
    
        while left < right:
            mid = left + (right - left) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left