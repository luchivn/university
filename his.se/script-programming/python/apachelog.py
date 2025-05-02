#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 4
# DATE OF LAST CHANGE: 2025-05-02
#-----------------------------------------------

import re

def aggregatelog(filename):
    keyvaluepairscounter = dict()
    # 'keyvaluepairscounter' must be a nested dictionary.
    # For example, it may contain the following information:
    #  keyvaluepairscounter['ip']['127.0.0.1']=511
    # to signify that IP address 127.0.0.1 was encountered 511 times
    # in the Apache log file.
    pattern = (
        r'(?P<IPaddress>\d{1,3}(?:\.\d{1,3}){3}) '
        r'- - \['
        r'(?P<DayOfMonth>\d{2})/'
        r'(?P<Month>\w{3})/'
        r'(?P<Year>\d{4}):'
        r'(?P<Hour>\d{2}):'
        r'(?P<Minute>\d{2}):'
        r'(?P<Seconds>\d{2}) '
        r'(?P<TimeZone>[+\-]\d{4})\] "'
        r'(?P<Method>\w+) '
        r'(?P<Path>[^ ]+) '
        r'HTTP/(?P<HTTPversion>\d+\.\d+)" '
        r'(?P<HTTPstatus>\d{3}) '
        r'(?P<RequestSize>\d+|-) '
        r'"(?P<Referrer>[^"]*)" '
        r'"(?P<UserAgent>[^"]*)"'
    )

    with open(filename) as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                groups = match.groupdict()
                for key, value in groups.items():
                    if key not in keyvaluepairscounter:
                        keyvaluepairscounter[key] = {}
                    if value not in keyvaluepairscounter[key]:
                        keyvaluepairscounter[key][value] = 1
                    else:
                        keyvaluepairscounter[key][value] += 1
            else:
                print(f"Line didn't match pattern: {line}")

    return keyvaluepairscounter
