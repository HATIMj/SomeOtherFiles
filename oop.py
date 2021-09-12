                                             #CLASSES AND METHODS



class Employee:
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary


    def printd(self):
        return f"My name is {self.name} and my salary  is {self.salary}. My age is {self.age}"
    @classmethod
    def new(cls,string):
        return cls(*string.split("-"))
       # p=string.split("-")
       # return cls(p[0],p[1],p[2])
    @classmethod
    def change_age(cls,new_age):
        cls.age=new_age
    @staticmethod
    def stat(n):
        return f"I am {n}"
class Programmer(Employee):
    def __init__(self,aname,aage,asalary,alanguages):
        self.name=aname
        self.age=aage
        self.salary=asalary
        self.languages=alanguages
    def jojo(self):
        return f"{self.name} had learned {self.languages}."




rohan=Employee("rohan","19","10000")
sohan=Employee("sohan","18","9000")
Khali=Employee.new("Khali-39-500000")
Khali.change_age(40)
karan=Programmer("Karan","18","90000",["python,c++"])
print(karan.jojo())