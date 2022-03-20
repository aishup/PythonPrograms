class Solution(object):
    def firstUniqChar(self, s):
        charFound = True
        for i in s:
            count = 0
            for j in s:
                #print(i,j)
                if i == j:
                    count+=1
            if count == 1:
                print("String Found",i)
                indexVal = s.index(i)
                return indexVal
                break
            else:
                continue
        return -1



p1 = Solution()
p1.firstUniqChar("loveleetcode")