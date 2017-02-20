
bread = 20
peanut_butter = 8
jelly = 6


if bread >=2 and peanut_butter >= 1 and jelly >= 1:
    number_sandwiches = min(bread/2, peanut_butter, jelly)
    bread -= number_sandwiches*2
    peanut_butter-= number_sandwiches
    jelly -= number_sandwiches
    num_pb_only = min(bread/2, peanut_butter) 
    print "I can make {0} peanut butter and jelly sandwiches and {1} peanut butter sandwiches.".format(number_sandwiches, num_pb_only)
    if bread%2 == 1:
        print "One could be open-faced"
    else:
        print "No odd bread."
else:
    print "Looks like I don't have a lunch today."
    if bread < 2:
        print "You're missing bread."
    else:
        print "Bread?  Check."
    if peanut_butter < 1:
        print "You're missing peanut butter."
    else:
        print "PB?  Check."
    if jelly < 1:
        print "You're missing jelly."
    else:
        print "Jelly?  Check."
    


