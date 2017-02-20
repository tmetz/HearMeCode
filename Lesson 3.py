'''
with open("C:\Users\koshi\Desktop\Python text files\states.txt","r") as states_file:
    states = states_file.read().split("\n")

state_names = []
state_abbrevs = []

for index, state in enumerate(states):
    states[index] = state.split("\t")

for state_pair in states:
    state_abbrevs.append(state_pair[0])
    state_names.append(state_pair[1])

# print " ".join(state_abbrevs)

#with open("C:\Users\koshi\Desktop\Python text files\state-abbrev.txt", "w") as abbrev_file:
#    abbrev_file.write(" ".join(state_abbrevs))

#with open("C:\Users\koshi\Desktop\Python text files\state-long.txt", "w") as long_file:
#    long_file.write(" ".join(state_names))

#print state_abbrevs
#print state_names
'''

phonebook = {
    'Shannon': '202-555-1234',
    'Bridgit': '703-555-9876',
    'Christine': '410-555-1293'
}

phonebook['Mel'] = '301-555-1111'

#phonebook['Test'] = '301-555-1111'


print phonebook.get('Frank', 'That shit does not exist')
