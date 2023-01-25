class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here
        dir = 0
        top = 0
        down = r-1
        left = 0
        right = c-1

        res = []

        while top <= down and left <= right:
            if dir == 0:
                # travel left to right
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top += 1

            if dir == 1:
                # travel top to down
                for i in range(top, down+1):
                    res.append(matrix[i][right])
                right -= 1

            if dir == 2:
                # travel right to left
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if dir == 3:
                # travel down to top
                for i in range(down, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

            # update direction
            dir = (dir + 1) % 4
        return res


s = Solution()
r = 4
c = 4
matrix =[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15,16]]

result = s.spirallyTraverse(matrix,r,c)
print(result)



# steps:
# In this we have 4 pointers:
# Top -> Tracking rows
# Down -> Tracking rows in reverse
# Left -> Moving pointer from left to right
# Right -> Moving pointer from right to left.
