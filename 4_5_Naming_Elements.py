info = {'name':'Bob', 'ref':'Python', 'sys':'Mac'}
print('info:', type(info))
print('Dictionary:', info)

print('\nReference:', info['ref'])

del info['name']
print('\nDictionary after deleting name:', info)
info['user'] = 'Tom'
print('Dictionary after adding user:', info)

print('\nIs there a name key?','name' in info)