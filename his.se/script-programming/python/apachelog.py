#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 4
# DATE OF LAST CHANGE: 2025-04-29
#-----------------------------------------------

import re

def aggregatelog(filename):
    keyvaluepairscounter = dict()
    keyvaluepairscounter["IPaddress"] = {}
    keyvaluepairscounter["Method"] = {}
    # 'keyvaluepairscounter' must be a nested dictionary.
    # For example, it may contain the following information:
    #  keyvaluepairscounter['ip']['127.0.0.1']=511
    # to signify that IP address 127.0.0.1 was encountered 511 times
    # in the Apache log file.
    ip_pattern = r"\d{1,3}(\.\d{1,3}){3}"
    method_pattern = r'"(\w+)'
    unique_ips = 0
    most_popular_apps = 0
    with open(filename) as file:
        for line in file:
            #getting ips data
            ip = re.match(ip_pattern,line)
            ip = ip.group()
            if ip in keyvaluepairscounter["IPaddress"]:
                keyvaluepairscounter["IPaddress"][ip] += 1
                if int(keyvaluepairscounter["IPaddress"][ip]) > most_popular_apps:
                    most_popular = ip
                    most_popular_apps = keyvaluepairscounter["IPaddress"][most_popular]
            else:
                keyvaluepairscounter["IPaddress"][ip] = 1
                unique_ips += 1
            #getting https methods data
            method = re.search(method_pattern,line)
            if method:
                method = method.group(1)
                if method in keyvaluepairscounter["Method"]:
                    keyvaluepairscounter["Method"][method] += 1
                else:
                    keyvaluepairscounter["Method"][method] = 1
    #sort the methods in descendant order of occurences
    keyvaluepairscounter["Method"] = dict(sorted(keyvaluepairscounter["Method"].items(),key=lambda item: item[1],reverse=True))
    #print the results
    for i in keyvaluepairscounter["Method"]:
        print(f"{i}:",keyvaluepairscounter["Method"][i])
    print(f"Most popular IP address id {most_popular} with {most_popular_apps} occurrences")
    print("Number of unique IP addresses:", unique_ips)

    return keyvaluepairscounter

dictio = aggregatelog('access-small.log')
