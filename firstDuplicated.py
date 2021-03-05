def firstDuplicate(a):

    dicc = {}

    for i in range(len(a)):
        if a[i] not in dicc:
            dicc[a[i]] = 1
        else:
            dicc[a[i]] += 1
        
        if dicc[a[i]] == 2:
            return a[i]
    
    return -1

res = firstDuplicate([1,4,8,2,9,3,7,2,7,2,1,8,4])
print(res)