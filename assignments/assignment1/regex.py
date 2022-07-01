import re

#Find a list of all of the names in the following string using regex
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    names_found = re.findall("[A-Z]\w*(?=[^\w])", simple_string)
    print(names_found)

#Create a regex to generate a list of just the students who received a B in the course of assets/grades.txt
def grades():
    with open ("D:/Data Science/Introduction to Data Science/assignments/assignment1/assets/grades.txt", "r") as file:
    #with open ("assets/grades.txt", "r") as file:
        grades = file.read()
    counted_grades = []
    for item in re.finditer("([\w\s]*)(:\s)(\w)([\s]*)", grades):
        if (item.group(3) == 'B'):
            counted_grades.append(item.group(1))
    print(counted_grades)

#Convert assets/logdata.txt into a list of dictionaries
def logs():
    with open ("D:/Data Science/Introduction to Data Science/assignments/assignment1/assets/logdata.txt", "r") as file:
    #with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    dictionary = []
    pattern = """
    (?P<host>[\d.]*)
    (\ \-\ )
    (?P<user_name>[\w\d]*|-)
    (\ \[)
    (?P<time>.*)
    (\]\ \")
    (?P<request>.*)
    (\".*)
    """
    for item in re.finditer(pattern,logdata,re.VERBOSE):
        dictionary.append(item.groupdict())
    