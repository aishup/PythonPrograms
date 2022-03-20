class Solution(object):
    def sortedSquares(self, nums):
        i = 0
        while(i < len(nums)):
            nums[i] = nums[i] ** 2
            print(i,nums[i])
            i+=1
        nums.sort()

        return nums

            


p1 = Solution()
p1.sortedSquares([1,2,3,4])