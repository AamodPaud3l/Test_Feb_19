#Q3. Create a Student class and initialize it with name and roll number. Make methods to :
#  a. Display - It should display all informations of the student.
#  b. setAge - It should assign age to student
#  c. setMarks - It should assign marks to the student.

class Student:
    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno


    @classmethod
    def getObjFromString(cls, inp):
        name, rollno = inp.split("-")
        return cls(name, rollno)

    def Display(self):
       print("The name is {} and roll no is {} ".format(self.name,self.rollno))

    def setAge(self,age):
        return age
    def setMarks(self,marks):
        return marks

s=Student.getObjFromString('Aamod-603')
s.Display()
print(s.setAge(19))
print(s.setMarks(85))