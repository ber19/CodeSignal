def firstNotRepeatingCharacter(s):
    dicc = {}

    for i in range(len(s)):
        if s[i] not in dicc:
            dicc[s[i]] = 1
        else:
            dicc[s[i]] += 1
        
    for i in dicc:
        if dicc[i] == 1:
            return i

    return "_"

res = firstNotRepeatingCharacter("abacabad")

print(res)