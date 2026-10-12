sample_set = {'Prince', 'Techs'}
print('Data' in sample_set)

sample_set.add('Data')
print(sample_set)
print(len(sample_set))

sample_set.remove('Data')
print(sample_set)

# Dédoublonner une liste
list2 = [1, 3, 1, 5, 3]
print(list(set(list2)))

# Ensemble immuable
sample_set = frozenset(sample_set)
print(sample_set)