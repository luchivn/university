#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 2
# DATE OF LAST CHANGE: 2025-05-01
#-----------------------------------------------
from datetime import datetime
from unicodedata import normalize, combining
import re

bad_words = ["idiot","annbj","jimha","susbe","ingfr","marpe","rolhe","runli","marsa","cecho"]

# function to get current year
def year():
    current_datetime = datetime.now()
    return current_datetime.year%100

# function to decode letters
def normalize_letters(fusername):
    return ''.join(c for c in normalize('NFKD', fusername) if not combining(c))

# List for newly created accounts (order matters to match it with the name list provided by the student administration)
newaccounts = list()

'''function that generates usernames for all cases, even if the first name or last name is too short. Personally, i 
decided to fill the remaining letter spaces with the letter "f" that stands for "filler"'''
def check_length(first_name, last_name):
    if len(first_name) >= 3 and len(last_name) >= 2:
        return first_name[:3] + last_name[:2]
    elif len(first_name) >= 3 and len(last_name) < 2:
        return first_name[:3] + (last_name + 'f')[:2]
    elif len(first_name) < 3 and len(last_name) >= 2:
        if len(first_name) == 1:
            return (first_name + 'ff')[:3] + last_name[:2]
        else:
            return (first_name + 'f')[:3] + last_name[:2]
    else:
        if len(first_name) == 1:
            return (first_name + 'ff')[:3] + (last_name + 'f')[:2]
        else:
            return (first_name + 'f')[:3] + (last_name + 'f')[:2]

'''function that checks if the previously generated username is an offensive word or not, if it is, the function is
replacing the middle character with one letter from a to z, checking the validity for each letter one by one to avoid
the generation of another offensive username'''
def check_valid(fusername):
    valid = False
    fcounter = 0
    while not valid:
        if fusername in bad_words:
            fusername = fusername[:2] + chr(ord('a') + fcounter) + fusername[3:]
            fcounter += 1
        else:
            valid = True
    return fusername

'''function for username generation, validity checking and special cases fixes via other functions from above'''
def generate_username(fstudent):
    student_name = re.sub('\n', '', fstudent)
    student_name = re.sub(r',\s*', ',', student_name)
    student_name = student_name.split(',')
    student = re.sub('[\n -]', '', fstudent)
    student = normalize_letters(student)
    student = student.split(',')
    fusername = check_length(student[1], student[0]).lower()
    fusername = check_valid(fusername)
    return fusername, student_name

'''Read list of existing accounts, and not only, here I've implemented the whole mandatory part, from reading the student 
names from the file, encoding and normalizing them to creating and checking whether the new usernames are in the database
or not as well as checking if the same username doesn't appear twice amongst the new students and changing the conflict
resolution letter if that is the case'''
with open("existingaccounts.csv","r+") as existingaccountsfile:
    with open("newstudents.csv", encoding="utf-8") as newstudentsfile:
        newstudents_dict = {}
        newstudents = set()
        for line in newstudentsfile:
            if line.strip() == '':
                pass
            else:
                username,fullname = generate_username(line)
                username = str(year()) + username
                created = False
                counter = 0
                while not created:
                    new_username = chr(ord('a') + counter) + username
                    if new_username in existingaccountsfile or new_username in newaccounts:
                        counter += 1
                    else:
                        created = True
                        newaccounts.append(new_username)
                        newstudents_dict[f"{fullname[1]} {fullname[0]}"] = new_username
    for new_student in newstudents_dict:
        print(f"{new_student} ->", newstudents_dict[new_student])
