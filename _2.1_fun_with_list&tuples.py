
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst = len(a)  
for i in range(0, lst):  
    for j in range(0, lst-i-1):  
        if (a[j][-1] > a[j + 1][-1]):  
            temp = a[j]  
            a[j]= a[j + 1]  
            a[j + 1]= temp  
print(a)