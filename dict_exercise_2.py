contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Tammy Metz"] = {
    "twitter": "@KoshIII",
    "github": "https://github.com/tmetz"
}

contacts["Sarah Berlin"] = {
    "twitter": "@sarahberlin",
    "github": "https://github.com/sarahberlin"
}

contacts["Test User"] = {
    "twitter": "@whatever",
    "github": ""
}
# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

'''
for contact in sorted(contacts.keys()):
    print contact + "\'s info:"
    print "\ttwitter: " + contacts[contact]['twitter']
    print "\tgithubb: " + contacts[contact]['github']
'''

for key, value in sorted(contacts.items()):
    print "{0}\'s info:".format(key)
    for key2, value2 in value.items():
        print "\t{0}: {1}".format(key2, value2)

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner
