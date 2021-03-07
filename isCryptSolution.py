def isCryptSolution(crypt, solution):
    diccSol = dict(solution)
    sum1 = ''
    sum2 = ''
    resp = ''

    for i in range(len(crypt)):
        for letter in crypt[i]:
            if i == 0:
                sum1 += diccSol.get(letter)
            elif i == 1:
                sum2 += diccSol.get(letter)
            else:
                resp += diccSol.get(letter)
    
    if int(sum1) + int(sum2) != int(resp):
        return False
    elif len(sum1)>1 and sum1[0]=='0':
        return False
    elif len(sum2)>1 and sum2[0]=='0':
        return False
    elif len(resp)>1 and resp[0]=='0':
        return False
    else:
        return True

# isCryptSolution( ["SEND", "MORE", "MONEY"], [['O', '0'],
#                                              ['M', '1'],
#                                              ['Y', '2'],
#                                              ['E', '5'],
#                                              ['N', '6'],
#                                              ['D', '7'],
#                                              ['R', '8'],
#                                              ['S', '9']] )


# isCryptSolution( ["TEN", "TWO", "ONE"], [['O', '1'],
#                                          ['T', '0'],
#                                          ['W', '9'],
#                                          ['E', '5'],
#                                          ['N', '4']] )


isCryptSolution( ["WASD","IJKL","AOPAS"], [["W","2"], 
                                           ["A","0"], 
                                           ["S","4"], 
                                           ["D","1"], 
                                           ["I","5"], 
                                           ["J","8"], 
                                           ["K","6"], 
                                           ["L","3"], 
                                           ["O","7"], 
                                           ["P","9"]] )