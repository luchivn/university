#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 4
# DATE OF LAST CHANGE: 2025-05-01
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
    with open(filename) as file:
        for line in file:
            #getting ips data
            ip = re.match(ip_pattern,line)
            ip = ip.group()
            if ip in keyvaluepairscounter["IPaddress"]:
                keyvaluepairscounter["IPaddress"][ip] += 1
            else:
                keyvaluepairscounter["IPaddress"][ip] = 1
            #getting https methods data
            method = re.search(method_pattern,line)
            if method:
                method = method.group(1)
                if method in keyvaluepairscounter["Method"]:
                    keyvaluepairscounter["Method"][method] += 1
                else:
                    keyvaluepairscounter["Method"][method] = 1

    return keyvaluepairscounter
