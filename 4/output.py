import numpy as np
import math
import domains
from domains import Student,Course,Mark
def studentslist(NumStu):
    for Student in NumStu:
        print(Student)
def courseslist(NumCo):
    for Course in NumCo:
        print(Course)
def selectmark(NumStu,NumCo,NumMark):
    E = input("selected courses")
    for Mark in NumMark:
        if (Mark.courseID == int(E)):
        for Student in NumStu:
            if (Mark.ID == Student.ID):
                for Course in NumCo:
                if (Course.courseID == int(E)):
                print(f"student {Student.name} got {Mark.mark} in course  {Course.name}")
def totalmark(NumMark,NumStu):
    for Student in NumStu:
        count=0
        for Mark in NumMark:
            if (Student.ID == Mark.ID):
                m=[]
                etc=[]
                m= np.append(m,[Mark.mark],axis=0)
                count= count + Mark
import math
import domains
from domains import Student,Course,Mark

def students_list(Students):
    for Student in Students:
        print(Student)


def courses_list(Courses):
    for Course in Courses:
        print(Course)


def selected_mark(NumStu,NumCo,NumMark):
    E = input("courses available")
    for Mark in NumMark:
        if (Mark.courseID == int(E)):
            for Student in NumStu:
                if (Mark.ID == Student.ID):
                    for Course in NumCo:
                        if (Course.courseID == int(E)):
                            print(f"student {Student.name} have {Mark.mark} in course  {Course.name}")
def totalmark(NumMark,NumStu):
    for Student in NumStu:
        count=0
        for Mark in Marks:
            if (Student.ID == Mark.ID):
                m=[]
                etc=[]
                m= np.append(m,[Mark.mark],axis=0)
                etc= np.append(etc,[Mark],axis=0)
                count= count + Mark
        GPA= (m*etc)/count
        Student.gpa= GPA