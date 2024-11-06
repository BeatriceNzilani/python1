class Person:
    # properties/variables/attribites/xtics
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

        #behavour/function
    def study(self):
        print("Student is studying")

#creating an object
student1 = Person("John",23,"Male")
student2=Person("Beatrice",29,"Female")
student3=Person("Bob",23,"Male")
print(student1.name,student1.age,student1.gender)
print(student2.name,student2.age,student2.gender)
print(student3.name,student3.age,student3.gender)

student1.study()
student2.study()