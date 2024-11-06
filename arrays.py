courses =["MIT","CYBERSECURITY","Datascience"]
print(courses)

#Accssing an element in array
print(courses[1])

#looping through ana element

for y in courses:
    print("Courses is ",y)

    #adding a new element

courses.append("Web development")
print(courses)

#deleting an element
courses.remove("MIT")
print(courses)

