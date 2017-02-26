import csv

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

survey_dict = {
    }

output_string = "name,email,phone,department,position,twitter,github"

with open("C:\\Users\\koshi\\Desktop\\Python text files\\survey.csv","r") as survey_file:
    survey_info = csv.DictReader(survey_file)
    for row in survey_info:
        survey_dict[row["email"]] = [row["twitter"], row["github"]]
        

with open("C:\\Users\\koshi\\Desktop\\Python text files\\all_employees.csv","r") as employees_file:
    employee_info = csv.DictReader(employees_file)
    for row2 in employee_info:
        output_string += "{0},{1},{2},{3},{4},".format(row2["name"],row2["email"],row2["phone"],row2["department"],row2["position"])
        if row2["email"] in survey_dict:
            emp_info = survey_dict[row2["email"]]
            print "{0} took the survey!  Here is her contact information: Twitter: {1} Github: {2} Phone: {3}".format(row2["name"],emp_info[0],emp_info[1], row2["phone"])
            output_string += "{0},{1}".format(emp_info[0],emp_info[1])
        else:
            output_string += "None, None"
with open("C:\\Users\\koshi\\Desktop\\Python text files\\all_employees2.csv", "w") as output_file:
    output_file.write(output_string)

# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github
