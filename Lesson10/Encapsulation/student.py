class Student:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name



    def set_name(self, name):
         self.__name = name


    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age


student1 = Student("Orges", 21)

print("Name:", student.get_name())
student1.set_name("Labeat")
print("Updated Name", student1.get_name())

print("Age:", student.get_age())
student1.set_age("22")
print("Updated Age", student1.get_age())