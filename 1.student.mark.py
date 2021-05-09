def costudents():
    count = int(input("number of student"))
    return count


def student():
    print("Enter Student Info : ")
    id = input(" ID : ")
    name = input(" Name : ")
    DOB = input(" DOB : ")
    C = {"id": id, "name": name, "DOB": DOB}
    return C



Students = []
count = costudents()
for i in range(0,count):
    C = student()
    Students += [C]

def students_list(Students):
    for C in Students:
        print(f"id {C['id']},name is {C['name']},DOB is {C['DOB']} ")




def cocourse():
    count = int(input("Number of courses  in the semester "))
    return count


def course():
    print("Enter Course Infor : ")
    id = input(" ID : ")
    name = input(" Name : ")
    A = {"id": id, "name": name}
    return A



courses =[]
count =cocourse()
for i in range(0,count):
    A = course()
    Courses = [A] + 1


def courseslist(courses):
    for A in courses:
        print(f"id {A['id']},name is {A['name']} ")



def addmark():
    Sid = input("input student id")
    Cid = input("course id:")
    m = input("mark:")
    B = {"Sid": Sid,"Cid": Cid, "mark": m }
    return B



Marks =[]
count = input("the number of mark you want to input ?")
for i in range(0,int(count)):
    B = addmark()
    Marks += [B]


def prmark():
    for B in Marks:
        print(f"student id is{B ['Sid']},course id is {B['Cid']},the mark of course is{B['mark']}")

def selPrint(Marks,courses,Students):
    E = input("courses selected ")
    for A in Students:
        for B in courses:
            for C in Marks:
                if E == B['id']:
                    if E == C['Cid']:
                        print(f"the student name is {A['name']}, the mark is {C['mark']}")