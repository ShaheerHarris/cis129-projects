#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

