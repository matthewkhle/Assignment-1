# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# --> add your Python code here
# 1y, 2pb, 3ppb
# 1m, 2h
# 1no, 2yes
# 1reduced, 2normal


# ORIGNAL HARD CODED DATA
# X = [
#     [1, 1, 1, 1],
#     [2, 1, 1, 2],
#     [3, 1, 1, 1],
#     [3, 1, 1, 2],
#     [2, 1, 2, 2],
#     [1, 1, 2, 2],
#     [1, 2, 1, 1],
#     [3, 1, 2, 1],
#     [2, 2, 1, 1],
#     [1, 1, 2, 1]
# ]


# Updated AFTER SUBMISSION (3/1/2021)
for instance in db:
    Xtemp = []

    if instance[0] == 'Young':
        Xtemp.append(1)
    elif instance[0] == 'Presbyopic':
        Xtemp.append(2)
    elif instance[0] == 'Prepresbyopic':
        Xtemp.append(3)

    if instance[1] == 'Myope':
        Xtemp.append(1)
    elif instance[1] == 'Hypermetrope':
        Xtemp.append(2)

    if instance[2] == 'No':
        Xtemp.append(1)
    elif instance[2] == 'Yes':
        Xtemp.append(2)

    if instance[3] == 'Normal':
        Xtemp.append(1)
    elif instance[3] == 'Reduced':
        Xtemp.append(2)

    X.append(Xtemp)


# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> addd your Python code here


# ORIGNAL HARD CODED DATA
# Y = [
#     2,
#     2,
#     2,
#     1,
#     1,
#     1,
#     2,
#     2,
#     2,
#     1
# ]

    # Updated AFTER SUBMISSION (3/1/2021)
    if instance[4] == 'Yes':
        Y.append(1)
    elif instance[4] == 'No':
        Y.append(2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=[
               'Yes', 'No'], filled=True, rounded=True)
plt.show()
