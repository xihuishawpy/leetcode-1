class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            res.extend(matrix[top][i] for i in range(left, right))
            top += 1
            # get every i in the right col
            res.extend(matrix[i][right - 1] for i in range(top, bottom))
            right -= 1
            if left >= right or top >= bottom:
                break
            # get every i in the bottom row
            res.extend(matrix[bottom - 1][i] for i in range(right - 1, left - 1, -1))
            bottom -= 1
            # get every i in the left col
            res.extend(matrix[i][left] for i in range(bottom - 1, top - 1, -1))
            left += 1

        return res
