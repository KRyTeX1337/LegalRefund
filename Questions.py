import Question


class Questions:
    def __init__(self):
        self.questionList = []

    def createQuestions(self):
        # 0
        self.addQuestion(
            Question.Question("Zu welchem Grund haben Sie die Ware gekauft?",
                              "Ich habe die Ware gekauft, um sie privat zu verwenden.",
                              "Ich benötige die Ware für den Betrieb eines Unternehmens."))
        # 1
        self.addQuestion(
            Question.Question("Wer hat Ihnen die Ware verkauft?",
                              "Mein*e Vertragspartner*in verkauft die Ware als Unternehmer*in in einem Online-Shop.",
                              "Es handelt sich um eine Privatperson. Diese verkauft die Ware gelegentlich und nicht langfristig."))
        # 2
        self.addQuestion(
            Question.Question("Haben Sie die Ware in einem Onlineshop gekauft?",
                              "Ich habe die Ware in einem Online-Shop bestellt.",
                              "Ich habe die Ware nicht in einem Online-Shop bestellt."))
        # 3
        self.addQuestion(
            Question.Question(
                "War der/die Verkäufer*in vor Ort, als Sie den Vertrag in einem Onlineshop geschlossen haben?",
                "Ich habe den Kauf getätigt, während der/die Unternehmer*in anwesend war",
                "Der/die Unternehmer*in war nicht anwesend, als ich den Kauf getätigt habe."))
        # 4
        self.addQuestion(
            Question.Question(
                "Sind 14 Tage vergangen, seit die Ware an Sie oder eine Abholstation geliefert wurde?",
                "Seit der Lieferung sind bereits mehr als 14 Tage vergangen.",
                "Die Rücktrittsfrist von 14 Tagen ist noch nicht verstrichen."))
        # 5
        self.addQuestion(
            Question.Question(
                "Haben Sie binnen der Rücktrittsfrist dem/der Verkäufer*in Ihren Rücktritt bekannt gegeben?",
                "Ich habe den/die Verkäufer*in von meinem Rücktritt informiert.",
                "Eine solche Erklärung habe ich nicht abgegeben"))
        # 6
        self.addQuestion(
            Question.Question(
                "Wurden Sie über Ihr gesetzliches Rücktrittsrecht vor der Bestellung informiert?",
                "Ich habe eine Widerrufsbelehrung erhalten.",
                "Eine Widerrufsbelehrung wurde weder auf einer Seite vor dem Bestellbutton, in den AGB, noch mit der Lieferung bereitgestellt."))

    def addQuestion(self, question):
        self.questionList.append(question)

    def jsonable(self):
        return self.__dict__
