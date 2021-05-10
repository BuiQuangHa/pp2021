import os
import domain
from domain import Student,Course,Mark,NumStu,NumCo,NumMark
import os.path



def addStudent():
    NumStu =[]
    count= int(input("Number of students"))
    for i in range(0,count):
        Name= input ("Student name:")
        BD = input ("Birthday:")
        ID = int (input("Student ID :"))
        s = Student(Name, BD, ID)
    # not done yet, still working on it

    def getcourseID(self):
        return self.courseID


class Mark:
    def __init__(self, ID, courseID, Mark):
        self.ID = ID
        self.courseID = courseID
        self.Mark = Mark
        

    def __str__(self):
        return f"student {self.ID} got {self.Mark} in {self.courseID}"