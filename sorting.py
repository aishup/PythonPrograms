#
# a =[9,5,8]
a = [9, 5, 7, 4, 6, 9, 8]
for i in range(len(a)):
    print(a[i])
    for j in range(len(a)):
        print(a[j])
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        print(a)


