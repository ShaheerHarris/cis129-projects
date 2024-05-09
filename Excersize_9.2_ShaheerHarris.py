#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:





# In[ ]:




