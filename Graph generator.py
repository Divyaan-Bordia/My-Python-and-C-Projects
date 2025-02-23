import matplotlib.pyplot as plt
import math
import numpy as np

# Starting Statements
print()
print("NOTE : This program will generate a graph")
print('NOTE : The number of numbers in x and y have to be the same')
print()

# X and Y input
print()
print("Enter the numbers you want on the X axis (separated by spaces)")
x = list(map(int, input().split()))
print()
print("Enter the numbers you want on the Y axis (separated by spaces)")
y = list(map(int, input().split()))
print()

if len(x) != len(y):
    print("The number of numbers in x and y have to be the same")
    print("Please try again")
    quit()

# X and Y label input
print()
print("Enter the label for the X axis")
x_label = input()
print()
print("Enter the label for the Y axis")
y_label = input()
print()

# Title input
print("Enter the title of the graph")
title = input()

# Plotting the graph
plt.scatter(x, y)
plt.plot(x, y)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()