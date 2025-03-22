import matplotlib.pyplot as plt

# Starting Statements
print()
print("NOTE : This program will generate a line graph")
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

# Color input
print()
print("Enter the color of the graph")
print('Choices are - red, yellow, blue, green')
color = input(str())

if color not in ['red', 'yellow', 'blue', 'green']:
    print('ERROR :')
    print('Please enter a valid color')
    quit()

# Line spacing

print()
print('Do you want full line spacing or dashed line spacing?')
print('Choices are - full, dashed')
line_spacing = input(str())
if line_spacing == 'full':
    line_spacing = '-'
else:
    line_spacing = '--'

if line_spacing not in ['-', '--']:
    print('ERROR :')
    print('Please enter a valid line spacing')
    quit()

# Plotting the graph
plt.scatter(x, y, c=color)
plt.plot(x, y, c=color, linestyle=line_spacing)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()
