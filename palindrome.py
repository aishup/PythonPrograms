from audioop import reverse


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        # Method 1
        xList = [i for i in str(x)]
        xList.reverse()
        reversedX = "".join(xList)
        print(reversedX)
        if str(x) == reversedX:
            return True
        else:
            return False
        """
        #Method 2
        xReversed = str(x)[::-1]
        if str(x) == xReversed:
            return True
        else:
            return False
x1 = Solution()
print(x1.isPalindrome(-1234))