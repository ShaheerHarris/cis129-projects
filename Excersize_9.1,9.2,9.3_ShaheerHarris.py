import os

# Checking if file exists
if not os.path.exists("grades.txt"):
    # Creating file if not
    print("File doesn't exist. Creating 'grades.txt'.")
    file = open("grades.txt", 'w')
else:
    # If the file exists, open it
    print("File exists. Opening 'grades.txt'.")
    file = open("grades.txt", 'a')

print('Enter any number of grades (-1 to quit)')

# Inputing the grades
while True:
    grade = int(input())
    if grade == -1:
        break
    else:
        file.write(f'{grade}\n')

file.close()

#Excersize 9.2

import os

# Checking if file exists
if not os.path.exists("grades.txt"):
    # Creating file if not
    print("File doesn't exist. Please run the previous code to create 'grades.txt'.")
else:
    # If the file exists, open it
    print("File exists. Opening 'grades.txt'.")

    # Open the grades.txt file in read mode
    file = open("grades.txt", 'r')

    # Initializing variables
    total = 0
    count = 0
    grades = []

    # Read grades from the file
    for line in file:
        grade = int(line.strip()) 
        grades.append(grade)
        total += grade
        count += 1

    file.close()

    # Display individual grades
    print("Individual grades:")
    for grade in grades:
        print(grade)

    # Calculations
    if count > 0:
        average = total / count
        print("Total:", total)
        print("Count:", count)
        print("Average:", average)
    else:
        print("No grades found in the file.")

#Excersize 9.3

import os
import csv

# Function for student data
def input_student_data():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    exam1_grade = int(input("Enter exam 1 grade: "))
    exam2_grade = int(input("Enter exam 2 grade: "))
    exam3_grade = int(input("Enter exam 3 grade: "))
    return (first_name, last_name, exam1_grade, exam2_grade, exam3_grade)

# Checking file exists
if not os.path.exists("grades.csv"):
    # Creating file if not
    print("File doesn't exist. Creating 'grades.csv'.")
    with open("grades.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1 Grade", "Exam 2 Grade", "Exam 3 Grade"])
else:
    # If file exists
    print("File exists. Opening 'grades.csv'.")

# Inputing the student data
while True:
    student_data = input_student_data()
    with open("grades.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)
    
    # Ask if there are more students
    more_students = input("Do you want to enter data for another student? (yes/no): ").lower()
    if more_students != 'yes':
        break

print("Student records are written to 'grades.csv'.")
