class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1new=l2new=""
        for i in range(len(l1)-1,-1,-1):
            l1new += str(l1[i])
        for j in range(len(l2)-1,-1,-1):
            l2new += str(l2[j])
        result = int(l1new)+int(l2new)
        #print(result)
        output = []
        for i in str(result):
           output.append(i)
        #print(output)
        return output.reverse()

p1 = Solution()
p1.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])

        
        