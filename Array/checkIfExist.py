arr = [2,4,5,3]

class Solution(object):
    def checkIfExist(self, arr):
        if arr.count(0) == 2:
            return True
        arr = list(set(arr))
        print(arr)
        if len(arr) ==  1 and arr[0] == 0: return True
        for i in arr:
            for j in arr:
                if i == j:
                    pass
                else:
                    print("i,j-->",i,j)
                    result = j * 2
                    print("result-->",result)
                    if i == result:
                        return True
        return False




p1 = Solution()
p1.checkIfExist(arr)
