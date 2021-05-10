class Student:
    
    def __init__(self, Name, BD, ID):
        self.Name = Name
        self.BD = BD
        self.ID = ID

    def __str__(self):
        return f"{self.Name} - {self.ID} - {self.BD}"

    def getID(self):
        return self.ID


class Course:
    def __init__(self, Name, courseID,):
        self.Name = Name
        self.courseID = courseID
    def __str__(self):
        return f"ID of the course: {self.courseID}, Course name :{self.Name}"

    def getcourseID(self):
        return self.courseID


class Mark:
    def __init__(self, ID, courseID, Mark):
        self.ID = ID
        self.courseID = courseID
        self.Mark = Mark
        

    def __str__(self):
        return f"Student ID {self.ID} got {self.Mark} in {self.courseID}"