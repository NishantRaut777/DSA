class Solution:
    def sumOfMatrix(self, N, M, Grid):
        # code here
        sum = 0
        for i in range(N):
            for j in range(M):
                sum += Grid[i][j]

        return sum


s = Solution()
Grid = [[1,0,1],
        [-8,9,-2]]

result = s.sumOfMatrix(2,3,Grid)
print(result)