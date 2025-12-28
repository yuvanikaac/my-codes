#EXERCISE:1 - AREA OF THE RECTANGLE
length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))
area = length*width
print(f"The area of the rectangle with {length} and {width} is:{area} cm")

#EXERCISE:2 - SHOPPING CART PROGRAM
item = input("Enter the name of the item: ")
price = int(input("Enter the price of one item: "))
quantity = int(input("Enter the number of items taken: "))
total = price*quantity
print(f"The total price for the {quantity} {item} is: {total}")

#EXERCISE:3 - Write a program to calculate the area of a square by getting the side length from the user
side = int(input("Enter the length of one side:"))
area = side*side
print(f"The area of the square having the side {side} is {area}")

#EXERCISE:4 -Write a program to calculate the perimeter of a rectangle using length and width entered by the user.
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
perimeter = 2*(length+width)
print("The perimeter of the rectangle with length",length,"and width",width,"is: ",perimeter)

#EXERCISE:5 -Write a program to calculate simple interest using principal, rate of interest, and time entered by the user.
p = float(input("Enter the principle amount : "))
t = int(input("Enter the time period in year : "))
r = int(input("Enter the rate of interst in digits: "))
si =(p*t*r)/100
print(f"the simple interest is : {si}")

#EXERCISE:6 -Write a program to calculate a person’s age using birth year and current year entered by the user.
b = int(input("Enter your birth year: "))
c = int(input("Enter the current year: "))
age = c-b
print(f"Your age is: {age} ")

#EXERCISE:7 -Write a program to calculate the area of a circle using radius entered by the user.
radius = int(input("Enter the radius of the circle :"))
area = 3.14*radius*radius
print("The area of circle with radius",radius,"is: ",area)


#EXERCISE:8 - Write a program to calculate the total salary using basic salary and bonus entered by the user.
bs = float(input("Enter the basic salary in a month: "))
bonus = int(input("Enter the bonus amount: "))
ts = bs+bonus
print("the total salary is : ",ts)

#EXERCISE:9 -Write a program to calculate the final price of a product after adding GST based on price and GST percentage entered by the user.
product = input("Enter the product:")
price = int(input("Enter the price of the product: "))
gst = (price*18)/100
tp = gst + price
print("The total price of the product after adding gst :",tp)

#EXERCISE:10 -Write a program to convert weight from kilograms to grams using user input.
weight = int(input("Enter the weight in kilogram: "))
gram = weight*1000
print(f"The weight in grams is: {gram}")


#EXERCISE:11 -Write a program to convert time from hours to minutes using user input.
time = int(input("Enter the time in hours: "))
min = time*60
print(f"The time in minutes is: {min}")

#EXERCISE:12 -Write a program to calculate the average of  three numbers entered by the user.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
avg=(n1+n2+n3)/3
print("The average is: ",avg)

#EXERCISE:13 -Write a program to calculate the remaining bank balance after withdrawing an amount entered by the user.
deposit = float(input("Enter the total account balance: "))
wd = float(input("Enter the amount withdrawn: "))
result = deposit-wd
print("The balance in the account is : ",result)

#EXERCISE:14 -Write a program to calculate the total marks of five subjects entered by the user.
s1 = int(input("Enter the mark in first subject: "))
s2 = int(input("Enter the mark in second subject: "))
s3 = int(input("Enter the mark in third subject: "))
s4 = int(input("Enter the mark in fourth subject: "))
s5 = int(input("ENter the mark in fifth subject: "))
sum = s1+s2+s3+s4+s5
print("The sum of marks of five subjects is :",sum)
