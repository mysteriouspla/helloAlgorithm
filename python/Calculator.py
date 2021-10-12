# Welcome to pyhack calculator

num_1 = float(input("Enter the first number "))
num_2 = float(input("Enter the second number "))

print("Please select operation which you want to do: ")

operator = int(input("Type 1-Addition, 2-Substration, 3-Multiplication, 4-Division " ))

if operator == 1:
    a = num_1 + num_2
    a = round(a,2)
    print(a)
elif operator == 2:
    b = num_1 - num_2
    b = round(b,2)
    print(b)
elif operator == 3:
    c = num_1 * num_2
    c = round(c,2)
    print(c) 
elif operator == 4:
    d = num_1 / num_2
    d = round(d,2)
    print(d)       
else:
    print("Invalid Input")
    
   