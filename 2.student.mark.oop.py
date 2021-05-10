class Student:
    
    def __init__(self, name, BD, ID):
        self.Name = Name
        self.BD = BD
        self.ID = ID

    def getID(self):
        return self.ID

    def getName(self):
        return self.Name

    def getBD(self):
        return self.BD

    def inputID(self, ID):
        self.ID = ID

    def inputName(self, Name):
        self.Name = Name

    def inputBD(self, BD):
        self.BD = BD

class Course:
    def __init__(self, Name, courseID):
        self.Name = Name
        self.courseID = courseID

    def __str__(self):
        return f"{self.Name}{self.courseID}"

    def getcourseID(self):
        return self.courseID


class Mark:
    def __init__(self, Sid, courseID, mark):
        self.ID = ID
        self.courseID = courseID
        self.Mark = Mark


    def __str__(self):
        return f"student {self.ID} got {self.Mark} in course {self.Name} with the ID {self.courseID}"

def addStudent():
    NumStu =[]
    count= int(input("Number of students"))
    for i in range(0,count):
        Name= input ("Name:")
        BD = input ("Birthday:")
        ID = int (input("Student ID :"))
        s = Student(Name, BD, ID)
        NumStu.append(s)
    return NumStu

def addCourse():
    NumCo =[]
    count = int(input("number of courses"))
    for i in range(0,count):
        Name = input("name")
        courseID = int(input("course ID"))
        c = Course(name, courseID)
        NumCo.append(c)
    return NumCo

def addMark():
    NumMark=[]
    option= input("Press info :")
        if (option == "info" ):
            ID = int(input("Student ID:"))
            courseID = int(input("Course ID:"))
            Mark= int(input(" Mark:"))
            m = Mark(ID,courseID,Mark)
            NumMark.append(m)
        if (option !="info") :
            print ("I said: PRESS INFO!!!!!")
        else: break
    return NumMark

def studentslist(NumStu):
    for Student in Students:
        print(Student)

def courseslist(NumCo):
    for Course in Courses:
        print(Course)

def markslist(NumStu,NumCo,NumMark):
    E = input("selected courses")
    for Mark in NumMark:
        if (Mark.courseID == int(E)):
           for Student in NumStu:
             if (Mark.ID == Student.ID):
              for Course in NumCo:
                if (Course.courseID == int(E)):
                  print(f"student {Student.name} have {Mark.mark} in course  {Course.name1}")
def main():
    NumStu = addStudent()
    NumCo = addCourse()
    NumMark = addMark()
    students_list(NumStu)
    courses_list(NumCo)
    markslist(NumStu,NumCo,NumMark)
if __name__ == "__main__":
    main()