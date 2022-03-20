class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxones = result = 0
        nums_len = len(nums)
        arr_len = nums_len-1
        if  nums_len == 1 and nums[0] == 0:  return 0
        if nums_len == 1 and nums[0] == 1: return 1
        if nums_len > 1:
            for i in range(nums_len):
                if nums[i] == 0:
                    if result < maxones:
                        result = maxones
                    maxones = 0  
                else:
                    maxones +=1
                if result < maxones:
                    result = maxones
        return result

p1 = Solution()
p1.findMaxConsecutiveOnes([1,1,0,1,1,1])