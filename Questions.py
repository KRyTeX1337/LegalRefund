import Question


class Questions:
    def __init__(self):
        self.questionList = []

    def createQuestions(self):
        self.addQuestion(Question.Question("Ist der Vertragsabschluss länger als 14 Tage her?","Ok","Nein"))
        self.addQuestion(Question.Question("Wurden Sie über das Bestehen eines Rücktrittsrechts informiert?","Wurde ich","Wurde ich nicht"))

    def addQuestion(self,question):
        self.questionList.append(question)

    def jsonable(self):
        return self.__dict__
