lista = [1,2,3,4,5,7,6]
tupla = (1,2,3,4,5,7,6)
string = "1234576"
sett = {1,2,3,4,5,7,6}
dicc = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5, 'siete':7, 'seis':6}

lista_dicc = [ [1,2], (3,[3.1,3.2]), '52', {(7.1,7.2),7} ]
dicc_lista = dict(lista_dicc)
for i in dicc_lista.items():
    k, v = i
    print(f'{k} -> {v}')