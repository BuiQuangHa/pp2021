import domain
from domain import Student,Course,Mark

def addStudent():
    NumStu =[]
    count= int(input("Number of students"))
    for i in range(0,count):
        Name= input ("Student name:")
        BD = input ("Birthday:")
        ID = int (input("Student ID :"))
        s = Student(name, BD, ID)
        NumStu.append(s)
    return NumStu


def addCourse():
    Courses =[]
    count = int(input("Number of courses"))
    for i in range(0,count):
        Name = input("Name")
        courseID = int(input("course ID"))
        c = Course(Name, courseID )
        NumCo.append(c)
    return NumCo


def addMark():
    NumMark=[]
    option= input("Type info  :")
        if (option == "info" ):
            ID = int(input("student ID:"))
            courseID  = int(input("course ID:"))
            Mark= int(input("the mark:"))
            m = Mark(ID,courseID,Mark)
            NumMark.append(m)
        if (option != "info"):
            print ("Error")
        else: break
    return NumMark