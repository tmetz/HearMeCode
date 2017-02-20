# Difficulty Level: Beginner

# Can you make Python print out the song for 99 bottles of beer on the wall?


# range(5) will give you a list containing [0, 1, 2, 3, 4]

# range(5, 10) will give you a list containing [5, 6, 7, 8, 9]

# range(5, 15, 3) will give you a list containing [5, 8, 11, 14]

# Helpful mnemonic: range(start, stop, step)

# Using range() and a loop, print out the song.  Your output should look like this:

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall
# 98 bottles of beer on the wall, 98 bottles of beer ...
# If one of those bottles should happen to fall, 97 bottles of beer on the wall



for beerbottle in range(1,99):
    print "{0} bottles of beer on the wall, {0} bottles of beer...\n If one of those bottles should happen to fall, {1} bottles of beer on the wall\n".format(100 - beerbottle, 99 - beerbottle)
    
