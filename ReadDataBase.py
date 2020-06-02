import json


class ReadDataBase:
    def __init__(self, directory: str = "dataBase/", students: str = "students.json", matters: str = "matters.json"):
        self.directory = directory
        self.studentsFileLoc = self.directory + students
        self.mattersFileLoc = self.directory + matters
        with open(self.studentsFileLoc, "r") as studentsFile:
            self.studentsData = json.load(studentsFile)
        with open(self.mattersFileLoc, "r") as mattersFile:
            self.mattersData = json.load(mattersFile)


    


