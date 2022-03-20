num_list = [300,400,500,3002,3003,71]

class find_even_no(object):
    
    def even_no(self,num_list):
        totEvenCnt = 0
        
        for i in range(len(num_list)):
            num_length = len(str(num_list[i]))
            if num_length%2 == 0:
                totEvenCnt += 1
        return totEvenCnt

p1 = find_even_no()
p1.even_no(num_list)
