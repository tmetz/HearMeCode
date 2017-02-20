# I accidentally overwrote this file while playing around with an interview question for Girls Who Code.
# This actually determines whether any 2 numbers in an array add to 100

import random

"""
Creates a list (array) of random numbers from 0 to 99
"""


myArray = []
foundMatch = 0

for i in range(0, 10):
    myArray.insert(i,random.randrange(1,100))
    print "{0}: {1}".format(i, myArray[i])


for j in range(0,len(myArray) - 1):
    for k in range (j+1, len(myArray) - 1):
        if myArray[j]+ myArray[k] == 100:
            print "{0} + {1} = 100!".format(myArray[j],myArray[k])
            foundMatch = 1
            j = len(myArray)
            break

if (foundMatch == 0):
    print "Sorry, nothing adds to 100."

