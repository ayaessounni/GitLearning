import copy

Dict1 = {'name': 'lee', 'age': 89, 'num': [1, 2, 8]}

Dict_copy = Dict1.copy()            # copie superficielle
Dict_dcopy = copy.deepcopy(Dict1)   # copie profonde
Dict2 = Dict1                       # simple référence (même objet)

Dict1['num'][1] = 6                 # on modifie la liste imbriquée

print('Dict1:', Dict1)
print('Dict_copy:', Dict_copy)
print('Dict_dcopy:', Dict_dcopy)
print('Dict2:', Dict2)
Dict1['age'] = 90
print(Dict_copy['age'], Dict2['age'])