nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
class Solution(object):
    def removeDuplicates(self, nums):
        i = j = 0
        while(i <= len(nums)):
            print(nums[i])
            if(nums[i] == nums[j]):
                nums[j] = nums[j+1]
            else:
                i+=1
                j=0
        print(nums)
p1 = Solution()
p1.removeDuplicates(nums)