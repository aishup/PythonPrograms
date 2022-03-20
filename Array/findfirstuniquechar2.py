class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for i in s:
            if i in s: 
                print(seen)   
            else:
                seen[i] = 1   
        print(seen) 

p1 = Solution()
p1.firstUniqChar("love")