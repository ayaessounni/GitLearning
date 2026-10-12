x = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(x)

# Deux autres façons de créer le même dictionnaire
x2 = dict(food='Spam', quantity=4, color='pink')
x3 = dict([("food", "Spam"), ("quantity", 4), ("color", "pink")])
print(x2)
print(x3)

# Copie
d = x.copy()
d['color'] = 'red'
print(x)
print(d)

# Accès aux éléments
print(d.get('name'))
print(d.get('name', 'The key value does not exist.'))
print(d.keys())
print(d.values())
print(d.items())

# Vider et supprimer
d.clear()
print(d)
del d
print(x['name'])