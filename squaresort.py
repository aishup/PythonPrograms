
class Solution(object):
    def sortedSquares(self, nums):
        result = list(i**2 for i in nums)
        result.sort()
        return result

p1 = Solution()
p1.sortedSquares([-4,-1,0,3,10])
