from MatterManager import MatterManager


class VisualInterface:
    def __init__(self):
        self.matterManager = MatterManager()
        self.on = True
        self.commands = {
            'Exit': self.quit,
            'printStu': self.printStu,
            'printMat': self.printMatters,
            'save': self.save,
            'createStu': self.createStu
        }

    @staticmethod
    def printingMessage(message: list):
        finalMessage = ''
        for string in message:
            finalMessage += string + '\n'
        print(finalMessage)

    def update(self):
        while self.on:
            print("Commands:")
            self.printingMessage(list(self.commands.keys()))
            command = str(input('>>>'))
            # noinspection PyArgumentList
            try:
                self.commands.get(command.split(' ')[0])(command)
            except Exception as e:
                print(e)
                print('invalid command')
        print('GoodBye 🍺🍺🍺')

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

    def printMatters(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            print('Matters:')
            self.printingMessage(self.matterManager.nameMatters)
        elif '-c' in instructions:
            if len(instructions) == 2:
                self.printingMessage(self.matterManager.mattersCodes)

    def printStu(self, command):
        instructions = command.split(' ')
        if len(instructions) == 1:
            self.printingMessage(self.matterManager.students)
        elif '-e' in instructions:
            n = instructions.index('-e')
            if '-n' in instructions:
                self.printingMessage(self.matterManager.studentByName(instructions[instructions.index('-n') + 1]))
            elif '-i' in instructions:
                self.printingMessage(self.matterManager.studentById(instructions[instructions.index('-i') + 1]))

    def createStu(self, command):
        name = str(input("Ingrese nombre del estudiante:\n>>>"))
        _id = str(input("Ingrese ID del estudiante:\n>>>"))
        self.matterManager.createStudent(name, _id)

    def quit(self, command):
        self.on = False
