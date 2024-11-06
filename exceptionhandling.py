try:
    print(number)

except:
    print("An error has ocurred")

try:
    num1 =20
    num2=0
    print(num1/num2)

except:
    print("cannot divide a number with a zero")
finally:
    print("success")