nums = [3,2,2,3]
val = 3
class Solution(object):
    def removeElement(self, nums, val):
        """
        nums.sort()
        i = 0
        if len(nums) > 1:         
            while(i < len(nums)):
                print("went inside lopp")
                if nums[i] == val:
                    nums.remove(val)
                else:
                    i+=1
        if len(nums) == 1:
            if nums[0] == val:
                nums.remove(val)
        """
        i=0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
            print(nums)
        return i
p1 = Solution()
p1.removeElement(nums,val)
                
