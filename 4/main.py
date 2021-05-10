import math
import numpy as np
import domains
from domains import Student,Course,Mark
import input as input
import output as output


def main():
    NumStu=input.addStudent()
    NumCo = input.addCourse()
    NumMark = input.addMark()
    output.studentslist(NumStu)
    output.courseslist(NumCo)
    output.totalmark(NumMark,NumStu)
    output.sorting(Students)
if __name__ == "__main__":
    main()