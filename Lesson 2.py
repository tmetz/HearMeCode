attendees = ['Shannon', 'Tammy', 'Rachel']

"""
print attendees[0]
print attendees[1]
print attendees[2]
print attendees[0:2]


print len(attendees)
number_of_attendees = len(attendees)
print number_of_attendees
"""

"""
attendees_ages = []
attendees_ages.append(28)
attendees_ages.append(27)
print attendees_ages
attendees_ages[0] = 29
print attendees_ages
"""



"""
print days_of_week
print len(days_of_week)
day = days_of_week.pop()
print day
print days_of_week

day = days_of_week.pop(3)
print day
print days_of_week
"""



"""
address = "1133 19th St NW Washington, DC 20036"
address_as_list = address.split(" ")
print address_as_list
print 'DC' in address_as_list
"""

"""
quadrant_NW = []
quadrant_NE = []
quadrant_SW = []
quadrant_SE = []
addresses = []
for i in range(3):
    addresses.insert(i, raw_input('Enter address:').upper())
    address_as_list = addresses[i].split(" ")
    if 'NW' in address_as_list:
        quadrant_NW.append(addresses[i])
    elif 'SW' in address_as_list:
        quadrant_SW.append(addresses[i])
    elif 'NE' in address_as_list:
        quadrant_NE.append(addresses[i])
    elif 'SE' in address_as_list:
        quadrant_SE.append(addresses[i])


print "SE Quadrant has {0} with length {1}".format(quadrant_SE, len(quadrant_SE))
print "SW Quadrant has {0} with length {1}".format(quadrant_SW, len(quadrant_SW))
print "NE Quadrant has {0} with length {1}".format(quadrant_NE, len(quadrant_NE))
print "NW Quadrant has {0} with length {1}".format(quadrant_NW, len(quadrant_NW))
"""



days_of_week = ['Monday', 'Tuesday']

days_of_week.append('Wednesday')
days_of_week.append('Thursday')
days_of_week.append('Friday')
days_of_week.append('Saturday')
days_of_week.append('Sunday')

months = ['January', 'February']
months.extend(['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

"""
print months

months.pop(0)
print months
months.insert(0, 'January')
print months
"""

"""
for day in days_of_week:   # day is the iterator
    print day
"""

for month in months:
    print month
    for week in range(1, 5):
        print "Week {0}".format(week)
        for day in days_of_week:
            print day
