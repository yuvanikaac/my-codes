# Q1 Get a name from the user and print it.
name = input(" Enter your name:")
print("Your name is :",name)


#Q2 Get an age from the user and print it.
age = int(input("Enter your age:"))
print("Your age is:",age)


#Q3 Get two numbers from the user and print both on separate lines.
n1=int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
print(n1)
print(n2)


#Q4 Get a decimal number from the user and print it.
d = float(input("Enter a decimal number:"))
print(f"The entered decimal number is {d}")

#Q5 Get two numbers from the user, add them, and print the result.
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum = a+b
print(f"The sum of {a} and {b} is {sum}")


#Q6 Get two strings from the user and print them together with a space.
s1 = input("Enter  first string ")
s2 = input("Enter  second string ")
print("The combined string is :")
print(f"{s1} {s2}")


# Q7 Get a value from the user, convert it into boolean, and print it.
v = input("Enter a value for converting it into boolean")
v = bool(v)
print(f"The converted boolean is {v}")


''' Q17 Get name and age from the user and print:

<name> is <age> years old

'''
name = input("Enter your name: ")
age = int(input("Enter you're age: "))
print(f"{name} is {age} years old")

#Q8 Get two numbers from the user, convert both to integers, add them, and print the result.
i1 = input("Enter your first number as string: ")
i2 = input("Enter your second number as string: ")
i1=int(i1)
i2=int(i2)
result = i1+i2
print(f"The sum of {i1} and {i2} is{result}")

#Q9 #Q8 Get two numbers from the user, convert both to integers, multiply them, and print the result.
f1 = input("Enter your first string: ")
f2 = input("Enter your second string: ")
f1 = int(f1)
f2 = int(f2)
result = f1*f2
print(f"The product of {f1} and {f2} is {result}")


'''Q10 Get three inputs:

* name (string)
* age (integer)
* height (float)

Print it '''
n = input("Enter your name :")
agee = int(input("enter your age: "))
height = float(input("Enter your height in cm: "))
print(f"{name} is {agee} years old and of height {height}")




