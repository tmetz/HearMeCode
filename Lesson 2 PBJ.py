

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = 17
peanut_butter = 13
jelly = 9
avail_sand = min(bread/2, peanut_butter, jelly)
i = 1

while avail_sand > 0:
    print "Making sandwich {0}".format(i)
    bread = bread - 2
    jelly = jelly - 1
    peanut_butter = peanut_butter - 1
    avail_sand = min(bread/2, peanut_butter, jelly)
    i = i + 1
    print "I have enough bread for {0} more sandwiches, enough pb for {1} more, and enough jelly for {2} more.".format(bread/2, peanut_butter, jelly)
if bread/2 < 1:
    print "All done; I ran out of bread."
elif peanut_butter == 0:
    print "All done; I ran out of pb."
elif jelly == 0:
    print "All done; I ran out of jelly."
else:
    print "Something strange happened."

#print "All done; only had enough bread for {0} sandwiches.".format(i - 1)
