class Solution:
    def matSearch(self, mat, N, M, X):
        for i in range(N):
            for j in range(M):
                if mat[i][j] == X:
                    return 1
        return 0


s = Solution()
N = 3
M = 3
mat = [[3 ,30 ,38], 
         [44 ,52 ,54], 
         [57 ,60 ,69]]
result = s.matSearch(mat,N,M,69)
print(result)


