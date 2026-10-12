S = 'python'
print(len(S))
print(S[0], S[1], S[-1])
print(S+'1', S*2)

S1 = 'Z' + S[1:]
print("S:%s, S1:%s" % (S, S1))

print(S.split('h'))
print(S.replace('py', 'PY'))
print(S.upper())
print('PYTHON'.lower())
print(' '.join(['life', 'is', 'short']))
print('%s %s %d' % ('hello', 'world', 12))
