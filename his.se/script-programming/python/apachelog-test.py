#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 4
# DATE OF LAST CHANGE: 2025-05-02
#-----------------------------------------------

import apachelog

# Use 'access-small.log' for developing your code,
# then use 'access.log' to see if your code is correct,
# i.e. produces the same numbers as shown in the lab instructions
# See 'apachelog.py' for a quick explanation what type of data 'evaluatedlogfile' is
log = apachelog.aggregatelog("access-small.log")
##log = apachelog.aggregatelog("access.log")

# TODO go through 'log' and print out all relevant information

#code for the extra points task
def get_most_popular(dictionary):
    most_popular = max(log[dictionary], key=log[dictionary].get)
    most_popular_apps = log[dictionary][most_popular]
    return most_popular, most_popular_apps


for key in log:
    mp, mpa = get_most_popular(key)
    print(f"{key}: {mp} with {mpa} occurences")

""" #code for the mandatory part
# sort the methods in descendant order of occurences
log["Method"] = dict(sorted(log["Method"].items(), key=lambda item: item[1], reverse=True))

# get the most popular IP address and its number of occurences
most_popular = max(log["IPaddress"],key = log["IPaddress"].get)
most_popular_apps = log["IPaddress"][most_popular]
# print the results
for i in log["Method"]:
    print(f"{i}:", log["Method"][i])
print(f"Most popular IP address is {most_popular} with {most_popular_apps} occurrences")
print("Number of unique IP addresses:", len(log["IPaddress"]))
"""
