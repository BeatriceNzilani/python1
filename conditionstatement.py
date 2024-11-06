
temp = int(input("Enter a temperature value: "))

if temp  < 25:
    print("it's too cold today")
else:
    print("it's too hot today")
    # A python program that checks three number and return the smallest
    num1 =float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    num3 = float(input("Enter your third number: "))

if num1<num2 and num1<num3:
    print(num1 ,"is the smallest number")
elif num2<num1 and num2<num3:
    print(num2 ,"is the smallest number")
elif num3 < num1 and num3 < num2:
    print(num3, "is the smallest number")
else :
    print(num3 ,"is not the smallest number")


# program to check whether a number is even or odd number

number = 79


if number % 2 ==0:
      print(number,"is an even number")
else:
      print(number,"is an odd number")


