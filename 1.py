def isCryptSolution(crypt, solution):
    diccSol = dict(solution)

    num1 = ''
    num2 = ''
    resp = ''
    cont = 0
    for word in crypt:
        for letter in word:
            if cont == 0:
                num1 += diccSol.get(letter)
            elif cont == 1:
                num2 += diccSol.get(letter)
            else:
                resp += diccSol.get(letter)
        cont += 1
    if int(num1) + int(num2) != int(resp):
        print('Mal')
        return False
    elif len(num1)>1 and num1[0]=='0':
        print('Mal')
        return False
    elif len(num2)>1 and num2[0]=='0':
        print('Mal')
        return False
    elif len(resp)>1 and resp[0]=='0':
        print('Mal')
        return False
    else:
        print('Bien')
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