import csv

# NOTE: I had to make capitalization changes in the input files for some of the
# non-state states to work (e.g. PUERTO RICO to Puerto Rico)

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu

with open("C:\Users\koshi\Desktop\Python text files\states.txt","r") as states_file:
    states = states_file.read().split("\n")

state_names = []
state_abbrevs = []

for index, state in enumerate(states):
    states[index] = state.split("\t")

for state_pair in states:
    state_abbrevs.append(state_pair[0])
    state_names.append(state_pair[1])

state_dict = dict(zip(state_names, state_abbrevs))

# Challenge 2: Save the HTML as states.html instead of printing it to screen.

with open("C:\Users\koshi\Desktop\Python text files\states.html", "w") as states_web_file:
    states_web_file.write("<select onChange = \"self.location.href=\'#\' + options[selectedIndex].value;\">\n")
    for i in range(1,len(states)):
        states_web_file.write("<option value = \"{0}\">{1}</option>\n".format(state_abbrevs[i], state_names[i]))
    states_web_file.write("</select>\n")


# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

    with open("C:\Users\koshi\Desktop\Python text files\state_info.csv","r") as state_info_file:
        state_info = csv.DictReader(state_info_file)
        for row in state_info:
            values = row.values()
            states_web_file.write("<table border = \"1\" id = \"{0}\">\n".format(state_dict[values[1]]))
            states_web_file.write("<tr>\n")
            states_web_file.write("<td colspan = \"2\">{0}</td>\n".format(values[1]))
            states_web_file.write("</tr>\n")
            states_web_file.write("<tr>\n")
            states_web_file.write("<td>Rank: {0}</td>\n".format(values[0]))
            states_web_file.write("<td>Percent: {0}</td>\n".format(values[3]))
            states_web_file.write("</tr>\n")
            states_web_file.write("<tr>\n")
            states_web_file.write("<td>US House Members: {0}</td>\n".format(values[2]))
            states_web_file.write("<td>Population: {0}</td>\n".format(values[4]))
            states_web_file.write("</tr>\n")
            states_web_file.write("</table>\n")

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge):
# When you make a choice from the drop-down menu, jump to that state's table.
