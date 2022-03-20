"""
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
"""
nums1 = [0]
m = 0
nums2 = [1]
n = 1
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0 and n == 0:
            #print("loop1")
            nums1 = []
        elif m == 0 and n == 1:
            #print("loop2")
            nums1 = []
            nums1.append(nums2[0])
            #print(nums1)
        elif m == 1 and n == 0:
            #print("loop3")
            val = nums1[0]
            nums1 = []
            nums1.append(val)
        elif m > 1 or n > 1:
            #print("loop4")
            popVal = len(nums1) - m
            for i in range(popVal):
                nums1.pop()
            for j in range(n):
                nums1.append(nums2[j])         
        if len(nums1) == m + n:
           # print("values equal")
            nums1.sort()
        nums1.sort()
        return nums1
        
p1 = Solution()
print(p1.merge(nums1,m,nums2,n))
