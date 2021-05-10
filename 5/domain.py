NumStu =[]
NumCo =[]
NumMark =[]
class Student:
    
    def __init__(self, Name, BD, ID):
        self.Name = Name
        self.BD= BD
        self.ID = ID

    def __str__(self):
        return f"{self.ID} - {self.Name} - {self.BD}"

    def getID(self):
        return self.ID


class Course:
    def __init__(self, Name, courseID,):
        self.Name = Name
        self.courseID = courseID
    def __str__(self):
        return f"Course ID {self.courseID} , name : {self.Name}"

    def getcourseID(self):
        return self.courseID


class Mark:
    def __init__(self, ID, courseID, Mark):
        self.ID = ID
        self.courseID = courseID
        self.Mark = Mark
        

    def __str__(self):
        return f"student {self.ID} got {self.Mark} in {self.courseID}"