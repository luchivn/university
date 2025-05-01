#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 1
# DATE OF LAST CHANGE: 2025-05-01
#-----------------------------------------------


# function that converts grades, either from ECTS to numbers, or numbers to ECTS
def convert_grade(grade):
    char_to_int = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0, 'F': 'F'}
    int_to_char = {'4': 'A', '3': 'B', '2': 'C', '1': 'D', '0': 'E'}

    if ord('0') <= ord(grade) <= ord('4'):
        return int_to_char[grade]
    elif ord('A') <= ord(grade) <= ord('F'):
        return int(char_to_int[grade])
    else:
        print("Invalid input. Try again.")

# function for reading subjects' names and ects from a file, storing them into a dictionary.
def reading_ects():
    ects = {}
    with open("exjobb.csv") as file:
        for line in file:
            subject = line.strip('\n')
            subject = subject.split(';')
            ects[subject[0]] = subject[1]
    return ects

"""function for processing the final grade. Returns the weighted final grade if the user have inputted correct values for 
all the assignments"""
def final_grade(subjects, ects):
    divide_by = 0
    grades = []
    grades_sum = 0
    for subject in subjects:
        divide_by +=  float(ects[subject])
        grades.append(convert_grade(subjects[subject]) * float(ects[subject]))
    for grade in grades:
        grades_sum += grade
    return "Weighted final grade: " + convert_grade(str(round((grades_sum / divide_by))))


'''function for getting users' grades, handling wrong char input errors, returning F as final grade in case one of the
grades is F, and calculating the final grade if that's the case'''
def get_grades(subjects):
    grades = {}
    f_flag = False
    for subject in subjects:
        attempts = 3
        while attempts:
            grade = input(f"{subject} Grade: ")
            if ord('A') <= ord(grade) <= ord('E'):
                grades[subject] = grade
                break
            elif grade == "F":
                f_flag = True
                break
            else:
                attempts -= 1
                if attempts:
                    print(f"Invalid input. Try again. ({attempts})")
                else:
                    return "Couldn't get it even after 3 tries? I give up. Good luck G"
    if f_flag:
        return 'Weighted final grade: F'
    return final_grade(grades, subjects)


print(get_grades(reading_ects()))
