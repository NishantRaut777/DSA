class Solution:
    def areMatricesidentical(self,N,Grid1,Grid2):
        #code here
        for i in range(N):
            for j in range(N):
                if Grid1[i][j] != Grid2[i][j]:
                    return 0
                else:
                    continue
        return 1

s = Solution()
Grid1 = [[1,2],[3,4]]
Grid2 = [[1,2],[3,4]]
result = s.areMatricesidentical(2,Grid1,Grid2)
print(result)