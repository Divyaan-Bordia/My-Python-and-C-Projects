import decimal 

print()
print("Unit Converter")
print()
choice = int(input("Enter 1 for km to miles, 2 for miles to km, 3 for kg to lbs, 4 for lbs to kg, 5 for Celsius to Fahrenheit, 6 for Fahrenheit to Celsius: "))
print()

if choice == 1:
    km = float(input("Enter km: "))
    miles = km * 0.621371
    print("Miles: " + str(miles))

elif choice == 2:
    miles = float(input("Enter miles: "))
    km = miles / 0.621371
    print("Km: " + str(km))

elif choice == 3: 
    kg = float(input("Enter kg: "))
    lbs = kg * 2.20462
    print("Lbs: " + str(lbs))
    
elif choice == 4:
    lbs = float(input("Enter lbs: "))
    kg = lbs / 2.20462
    print("Kg: " + str(kg))

elif choice == 5:
    celcius = float(input("Enter celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print("Fahrenheit: " + str(fahrenheit))

elif choice == 6: 
    fahrenheit = float(input("Enter fahrenheit: "))
    celcius = (fahrenheit - 32) * 5/9
    print("Celcius: " + str(celcius))

else:
    print("Invalid input")
    print()
    quit()

    exept :ValueError
    print("Invalid input")
    print()
    quit()
    

