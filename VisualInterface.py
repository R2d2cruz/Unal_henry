"""
VisualInterface:
        Give control by terminal for the user

Authors:
        Carlos Arturo Cruz Useche - 1001048369
        Diego Alejandro Campos Méndez - 1005753729

"""

from MatterManager import MatterManager

Exit = 'exit'
printStu = 'printStu'
printMat = 'printMat'
save = 'save'
createStu = 'createStu'
createMat = 'createMat'
Help = 'help'
orgSchedule = 'org'
getHelp = {
    Exit: "It uses to close the program. All changes don't save will be deleted",
    printStu: 'If it is alone, it print all the students Id.\n\nTheir special combination commands are:\n\n\t'
              + printStu + ' -e -n [name]\n\t\tIt print the student with name [name].\n\n\t' + printStu +
              ' -e -i [id]\n\t\tIt print the student tha have Id [id]',
    printMat: 'If it is alone, it print all the subject names.\n\nTheir special combination commands are:\n\n\t'
              + printMat + ' -c\n\t\tIt print all subject codes.',
    save: 'If it is alone, it save all changes.\n\nTheir special combination commands are:\n\n\t'
          + printStu + ' -e -s [studentId]\n\t\tIt save all changes for the student with the id [studentId].\n\n\t'
          + printStu + ' -e -m [subjectId]\n\t\tIt update the number of students in the subject with id [subjectId]',
    createStu: 'It create a new student',
    createMat: 'It create and save a new subject',
    orgSchedule: 'It organize automatic the students schedule'
}


class VisualInterface:
    def __init__(self):
        self.matterManager = MatterManager()
        self.on = True
        self.commands = {
            Exit: self.quit,
            printStu: self.printStu,
            printMat: self.printMatters,
            save: self.save,
            createStu: self.createStu,
            Help: self.help,
            createMat: self.createMat,
            orgSchedule: self.orgSchedule
        }

    @staticmethod
    def printingMessage(message: list):
        finalMessage = ''
        for string in message:
            finalMessage += string + '\n'
        print(finalMessage)

    def update(self):
        while self.on:
            command = str(input('>>>'))
            # noinspection PyArgumentList
            try:
                self.commands.get(command.split(' ')[0])(command)
            except Exception as e:
                print(e)
                print('invalid command')
                print('Write help to see the command')
        print('GoodBye 🍺🍺🍺')

    def help(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            print("Commands:")
            self.printingMessage(list(self.commands.keys()))
        elif len(instructions) == 2:
            print(instructions[1])
            print(getHelp.get(instructions[1]))

    def orgSchedule(self, command):
        self.matterManager.orgSchedule()

    def save(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            self.matterManager.saveAll()
            print('🍺🍺🍺')
        elif '-e' in instructions:
            n = instructions.index('-e')
            if instructions[n + 1] == '-s':
                if instructions[n + 2] in self.matterManager.students:
                    self.matterManager.saveIndividualStudentById(instructions[n + 2])
            elif instructions[n + 1] == '-m':
                self.matterManager.saveMatterNumStudents(instructions[n + 2])
        else:
            print('Error. Write ' + Help + ' [command] for read the documentation for a specific command')

    def printMatters(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            print('Matters:')
            self.printingMessage(self.matterManager.nameMatters)
        elif '-c' in instructions:
            if len(instructions) == 2:
                self.printingMessage(self.matterManager.mattersCodes)
        else:
            print('Error. Write ' + Help + ' [command] for read the documentation for a specific command')

    def printStu(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            self.printingMessage(self.matterManager.students)
        elif '-e' in instructions:
            if '-n' in instructions:
                self.printingMessage(self.matterManager.studentByName(instructions[instructions.index('-n') + 1]))
            elif '-i' in instructions:
                self.printingMessage(self.matterManager.studentById(instructions[instructions.index('-i') + 1]))
        else:
            print('Error. Write ' + Help + ' [command] for read the documentation for a specific command')

    # crea un nuevo estudiante desde el terminal
    def createStu(self, command):
        name = str(input('Ingrese nombre del estudiante:\n>>>'))
        _id = str(input('Ingrese ID del estudiante:\n>>>'))
        self.matterManager.createStudent(name, _id)

    # crea una nueva materia desde la terminal
    def createMat(self, command):
        name = str(input('Ingrese nombre de la materia:\n>>>'))
        _id = str(input('Ingrese ID de la materia:\n>>>'))
        maxStu = int(input('Ingrese el numero maximo de estudiantes:\n>>>'))
        owl = str(input('Ingrese nombre del docente:\n>>>'))
        value = int(input('Ingrese costo de creditos:\n>>>'))
        self.matterManager.createMatter(name, _id, value, owl, maxStu)

    def quit(self, command):
        self.on = False
