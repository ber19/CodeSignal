def rotateImage(a):
    res = list(zip(*a))
    res = [ list(tup[::-1]) for tup in res ] 
    return res
    


res = rotateImage([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9] ])

print(res)

