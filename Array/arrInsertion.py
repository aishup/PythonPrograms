
arr = [1,0,2,3,0,4,5,0]
class Solution(object):
    def duplicateZeros(self, arr):
        arrlen=len(arr)
        i=0
        while(i < arrlen):
            if arr[i] == 0:
                arr = arr[:i] + [0] + arr[i:arrlen-1]
                i+=2
            else:
                i+=1
        #arr = str(arr).replace(" ","")
        print( ",".join( str(x) for x in arr ))
        return(arr)
p1 = Solution()
p1.duplicateZeros(arr)

