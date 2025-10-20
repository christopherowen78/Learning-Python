party_goers = {'Andrew','Barbara','Carole','David'}
print('party_goers:', type( party_goers ))
print(len(party_goers), 'people are coming to the party.')

print('Did David go to the party?','David' in party_goers)
print('Did Kelly go to the party?','Kelly' in party_goers)

students = {'Andrew','Kelly','Lynn','David'}
commons = party_goers.intersection(students)
party_students = list(commons)

print('\nStudents at the party:', party_students)
print(len(party_students), 'students are at the party.')
print('First student at the party:', party_students[0])
print('Second student at the party:', party_students[1])