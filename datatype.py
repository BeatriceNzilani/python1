#how we get to categorize data

number =67 #INTERGER
second =67.09 #float
x ="hello world" #string
isPythonInteresting = True #boolean

#Data structure .multiple values stored in a single variable
cars=["BMW","FORD","G-WAGON"] #list-it's ordered  and also mutable/changeable
fruits=("banana","orange","mangoes")#tuple-ordered but unchangeable
countries={"kenya","uganda","tunisia"} #set-unordered and unchangeable
student={
    "name":"beatrice",
    "age":25,
    "gender":"female",
    "course":"Web Development",
}#Dictionary - key value pair



print(isPythonInteresting)
print(x)
print(second)
print(number)
#data structure
print(cars)
print(fruits)
print(countries)
print(student["name"])

#determine data typeof a variable

print(type(countries))
print(type(student))

#typecasting-converting from one datatype to another.
print(float(number))
print(int(second))