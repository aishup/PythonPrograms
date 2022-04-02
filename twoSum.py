class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# Brute Force Method
        """
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    tempTarget = nums[i] + nums[j]
                    if tempTarget == target:
                        output.append(int(i))
                        output.append(int(j))
                        #print(i,j,output)
                        return output
        """
#Hash Map Method(Dictionary in Python)
        hashmap ={}
        output = []
        for i in range(len(nums)):
            x = target - nums[i]
            if x not in hashmap:
                hashmap[nums[i]] = i
            else:
                output.append(hashmap[x])
                output.append(i)
                print(output)
                return output



if __name__ == '__main__':
    p1 = Solution()
    #p1.twoSum([2,7,11,15],9)
    p1.twoSum([3,2,4],6)