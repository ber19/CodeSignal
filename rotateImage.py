def rotateImage(a):
    res1 = zip(*a)
    res = []
    for i in res1:
        res.append(i[::-1])
    return res
    


res = rotateImage([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9] ])

print(res)

