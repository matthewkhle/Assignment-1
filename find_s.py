# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

print("\nThe initial value of hypothesis: ")
# representing the most specific possible hypothesis
hypothesis = ['0'] * num_attributes
print(hypothesis)

# find the first positive training data in db and assign it to the vector hypothesis
# --> add your Python code here
for instance in db:
    if instance[4] == 'Yes':  # check for 'Yes' in 5th index, positive
        for i in range(0, 3):
            hypothesis[i] = instance[i]
        break  # break out of for loop

# find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
# --> add your Python code here
for instance in db:
    if instance[4] == 'Yes':  # check for 'Yes' in 5th index, positive
        for i in range(0, 3):
            if instance[i] != hypothesis[i]:
                hypothesis[i] = '?'

print("\nThe Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:")
print(hypothesis, "\n")
